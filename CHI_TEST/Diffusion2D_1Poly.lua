print("############################################### LuaTest")
--dofile(CHI_LIBRARY)



--############################################### Setup mesh
chiMeshHandlerCreate()

newSurfMesh = chiSurfaceMeshCreate();
chiSurfaceMeshImportFromOBJFile(newSurfMesh,
        "CHI_RESOURCES/TestObjects/SquareMesh2x2Quads.obj",true)

--############################################### Extract edges from surface mesh
loops,loop_count = chiSurfaceMeshGetEdgeLoopsPoly(newSurfMesh)

line_mesh = {};
line_mesh_count = 0;

for k=1,loop_count do
    split_loops,split_count = chiEdgeLoopSplitByAngle(loops,k-1);
    for m=1,split_count do
        line_mesh_count = line_mesh_count + 1;
        line_mesh[line_mesh_count] =
        chiLineMeshCreateFromLoop(split_loops,m-1);
    end

end

--############################################### Setup Regions
region1 = chiRegionCreate()
chiRegionAddSurfaceBoundary(region1,newSurfMesh);
for k=1,line_mesh_count do
    chiRegionAddLineBoundary(region1,line_mesh[k]);
end

--############################################### Create meshers
chiSurfaceMesherCreate(SURFACEMESHER_PREDEFINED);
chiVolumeMesherCreate(VOLUMEMESHER_PREDEFINED2D);

chiVolumeMesherSetProperty(FORCE_POLYGONS,true);

--############################################### Execute meshing
chiSurfaceMesherExecute();
chiVolumeMesherExecute();

--############################################### Set Material IDs
vol0 = chiLogicalVolumeCreate(RPP,-1000,1000,-1000,1000,-1000,1000)
chiVolumeMesherSetProperty(MATID_FROMLOGICAL,vol0,0)


--############################################### Add materials
materials = {}
materials[0] = chiPhysicsAddMaterial("Test Material");

chiPhysicsMaterialAddProperty(materials[0],SCALAR_VALUE)
chiPhysicsMaterialSetProperty(materials[0],SCALAR_VALUE,SINGLE_VALUE,1.0)



--############################################### Setup Physics
phys1 = chiDiffusionCreateSolver();
chiSolverAddRegion(phys1,region1)
fftemp = chiSolverAddFieldFunction(phys1,"Temperature")
chiDiffusionSetProperty(phys1,DISCRETIZATION_METHOD,PWLC);
chiDiffusionSetProperty(phys1,RESIDUAL_TOL,1.0e-4)

--############################################### Set boundary conditions
--chiDiffusionSetProperty(phys1,BOUNDARY_TYPE,0,DIFFUSION_REFLECTING,1.0)
--chiDiffusionSetProperty(phys1,BOUNDARY_TYPE,1,DIFFUSION_VACUUM,2.0)
--chiDiffusionSetProperty(phys1,BOUNDARY_TYPE,2,DIFFUSION_REFLECTING,3.0)
--chiDiffusionSetProperty(phys1,BOUNDARY_TYPE,3,DIFFUSION_VACUUM,4.0)

--############################################### Initialize Solver
chiDiffusionInitialize(phys1)
chiDiffusionExecute(phys1)

slice2 = chiFFInterpolationCreate(SLICE)
chiFFInterpolationSetProperty(slice2,SLICE_POINT,0.0,0.0,0.025)
chiFFInterpolationSetProperty(slice2,ADD_FIELDFUNCTION,fftemp)

chiFFInterpolationInitialize(slice2)
chiFFInterpolationExecute(slice2)


line0 = chiFFInterpolationCreate(LINE)
chiFFInterpolationSetProperty(line0,LINE_FIRSTPOINT,-1.0,0.1,0.0)
chiFFInterpolationSetProperty(line0,LINE_SECONDPOINT, 1.0,0.1,0.0)
chiFFInterpolationSetProperty(line0,LINE_NUMBEROFPOINTS, 100)
chiFFInterpolationSetProperty(line0,ADD_FIELDFUNCTION,fftemp)

chiFFInterpolationInitialize(line0)
chiFFInterpolationExecute(line0)


ffi1 = chiFFInterpolationCreate(VOLUME)
curffi = ffi1
chiFFInterpolationSetProperty(curffi,OPERATION,OP_MAX)
chiFFInterpolationSetProperty(curffi,LOGICAL_VOLUME,vol0)
chiFFInterpolationSetProperty(curffi,ADD_FIELDFUNCTION,fftemp)

chiFFInterpolationInitialize(curffi)
chiFFInterpolationExecute(curffi)
maxval = chiFFInterpolationGetValue(curffi)

chiLog(LOG_0,string.format("Max-value=%.5f", maxval))

if (master_export == nil) then
    chiFFInterpolationExportPython(slice2)
    chiFFInterpolationExportPython(line0)
    local handle = io.popen("python3 ZPFFI00.py")
    local handle = io.popen("python3 ZLFFI10.py")

    chiExportFieldFunctionToVTK(fftemp,"ZPhi")
end
