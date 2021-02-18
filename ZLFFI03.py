import numpy as np
import matplotlib.pyplot as plt

def AddData0(data0):
  data0[50,0] = 0.010101
  data0[50,1] = 0
  data0[50,2] = 0.025
  data0[50,3] = 1.0101
  data0[50,4] = 0.294766
  data0[51,0] = 0.030303
  data0[51,1] = 0
  data0[51,2] = 0.025
  data0[51,3] = 1.0303
  data0[51,4] = 0.29445
  data0[52,0] = 0.0505051
  data0[52,1] = 0
  data0[52,2] = 0.025
  data0[52,3] = 1.05051
  data0[52,4] = 0.294134
  data0[53,0] = 0.0707071
  data0[53,1] = 0
  data0[53,2] = 0.025
  data0[53,3] = 1.07071
  data0[53,4] = 0.29356
  data0[54,0] = 0.0909091
  data0[54,1] = 0
  data0[54,2] = 0.025
  data0[54,3] = 1.09091
  data0[54,4] = 0.292609
  data0[55,0] = 0.111111
  data0[55,1] = 0
  data0[55,2] = 0.025
  data0[55,3] = 1.11111
  data0[55,4] = 0.291658
  data0[56,0] = 0.131313
  data0[56,1] = 0
  data0[56,2] = 0.025
  data0[56,3] = 1.13131
  data0[56,4] = 0.290507
  data0[57,0] = 0.151515
  data0[57,1] = 0
  data0[57,2] = 0.025
  data0[57,3] = 1.15152
  data0[57,4] = 0.288913
  data0[58,0] = 0.171717
  data0[58,1] = 0
  data0[58,2] = 0.025
  data0[58,3] = 1.17172
  data0[58,4] = 0.28732
  data0[59,0] = 0.191919
  data0[59,1] = 0
  data0[59,2] = 0.025
  data0[59,3] = 1.19192
  data0[59,4] = 0.285583
  data0[60,0] = 0.212121
  data0[60,1] = 0
  data0[60,2] = 0.025
  data0[60,3] = 1.21212
  data0[60,4] = 0.283333
  data0[61,0] = 0.232323
  data0[61,1] = 0
  data0[61,2] = 0.025
  data0[61,3] = 1.23232
  data0[61,4] = 0.281083
  data0[62,0] = 0.252525
  data0[62,1] = 0
  data0[62,2] = 0.025
  data0[62,3] = 1.25253
  data0[62,4] = 0.278749
  data0[63,0] = 0.272727
  data0[63,1] = 0
  data0[63,2] = 0.025
  data0[63,3] = 1.27273
  data0[63,4] = 0.275824
  data0[64,0] = 0.292929
  data0[64,1] = 0
  data0[64,2] = 0.025
  data0[64,3] = 1.29293
  data0[64,4] = 0.272899
  data0[65,0] = 0.313131
  data0[65,1] = 0
  data0[65,2] = 0.025
  data0[65,3] = 1.31313
  data0[65,4] = 0.269952
  data0[66,0] = 0.333333
  data0[66,1] = 0
  data0[66,2] = 0.025
  data0[66,3] = 1.33333
  data0[66,4] = 0.266328
  data0[67,0] = 0.353535
  data0[67,1] = 0
  data0[67,2] = 0.025
  data0[67,3] = 1.35354
  data0[67,4] = 0.262703
  data0[68,0] = 0.373737
  data0[68,1] = 0
  data0[68,2] = 0.025
  data0[68,3] = 1.37374
  data0[68,4] = 0.259079
  data0[69,0] = 0.393939
  data0[69,1] = 0
  data0[69,2] = 0.025
  data0[69,3] = 1.39394
  data0[69,4] = 0.254771
  data0[70,0] = 0.414141
  data0[70,1] = 0
  data0[70,2] = 0.025
  data0[70,3] = 1.41414
  data0[70,4] = 0.250417
  data0[71,0] = 0.434343
  data0[71,1] = 0
  data0[71,2] = 0.025
  data0[71,3] = 1.43434
  data0[71,4] = 0.246064
  data0[72,0] = 0.454545
  data0[72,1] = 0
  data0[72,2] = 0.025
  data0[72,3] = 1.45455
  data0[72,4] = 0.241066
  data0[73,0] = 0.474747
  data0[73,1] = 0
  data0[73,2] = 0.025
  data0[73,3] = 1.47475
  data0[73,4] = 0.235949
  data0[74,0] = 0.494949
  data0[74,1] = 0
  data0[74,2] = 0.025
  data0[74,3] = 1.49495
  data0[74,4] = 0.230832
  data0[75,0] = 0.515152
  data0[75,1] = 0
  data0[75,2] = 0.025
  data0[75,3] = 1.51515
  data0[75,4] = 0.225111
  data0[76,0] = 0.535354
  data0[76,1] = 0
  data0[76,2] = 0.025
  data0[76,3] = 1.53535
  data0[76,4] = 0.219191
  data0[77,0] = 0.555556
  data0[77,1] = 0
  data0[77,2] = 0.025
  data0[77,3] = 1.55556
  data0[77,4] = 0.21327
  data0[78,0] = 0.575758
  data0[78,1] = 0
  data0[78,2] = 0.025
  data0[78,3] = 1.57576
  data0[78,4] = 0.206792
  data0[79,0] = 0.59596
  data0[79,1] = 0
  data0[79,2] = 0.025
  data0[79,3] = 1.59596
  data0[79,4] = 0.200023
  data0[80,0] = 0.616162
  data0[80,1] = 0
  data0[80,2] = 0.025
  data0[80,3] = 1.61616
  data0[80,4] = 0.193253
  data0[81,0] = 0.636364
  data0[81,1] = 0
  data0[81,2] = 0.025
  data0[81,3] = 1.63636
  data0[81,4] = 0.185979
  data0[82,0] = 0.656566
  data0[82,1] = 0
  data0[82,2] = 0.025
  data0[82,3] = 1.65657
  data0[82,4] = 0.178312
  data0[83,0] = 0.676768
  data0[83,1] = 0
  data0[83,2] = 0.025
  data0[83,3] = 1.67677
  data0[83,4] = 0.170644
  data0[84,0] = 0.69697
  data0[84,1] = 0
  data0[84,2] = 0.025
  data0[84,3] = 1.69697
  data0[84,4] = 0.162531
  data0[85,0] = 0.717172
  data0[85,1] = 0
  data0[85,2] = 0.025
  data0[85,3] = 1.71717
  data0[85,4] = 0.153912
  data0[86,0] = 0.737374
  data0[86,1] = 0
  data0[86,2] = 0.025
  data0[86,3] = 1.73737
  data0[86,4] = 0.145294
  data0[87,0] = 0.757576
  data0[87,1] = 0
  data0[87,2] = 0.025
  data0[87,3] = 1.75758
  data0[87,4] = 0.136297
  data0[88,0] = 0.777778
  data0[88,1] = 0
  data0[88,2] = 0.025
  data0[88,3] = 1.77778
  data0[88,4] = 0.126669
  data0[89,0] = 0.79798
  data0[89,1] = 0
  data0[89,2] = 0.025
  data0[89,3] = 1.79798
  data0[89,4] = 0.117042
  data0[90,0] = 0.818182
  data0[90,1] = 0
  data0[90,2] = 0.025
  data0[90,3] = 1.81818
  data0[90,4] = 0.107114
  data0[91,0] = 0.838384
  data0[91,1] = 0
  data0[91,2] = 0.025
  data0[91,3] = 1.83838
  data0[91,4] = 0.0964171
  data0[92,0] = 0.858586
  data0[92,1] = 0
  data0[92,2] = 0.025
  data0[92,3] = 1.85859
  data0[92,4] = 0.0857206
  data0[93,0] = 0.878788
  data0[93,1] = 0
  data0[93,2] = 0.025
  data0[93,3] = 1.87879
  data0[93,4] = 0.0748113
  data0[94,0] = 0.89899
  data0[94,1] = 0
  data0[94,2] = 0.025
  data0[94,3] = 1.89899
  data0[94,4] = 0.0629827
  data0[95,0] = 0.919192
  data0[95,1] = 0
  data0[95,2] = 0.025
  data0[95,3] = 1.91919
  data0[95,4] = 0.0511541
  data0[96,0] = 0.939394
  data0[96,1] = 0
  data0[96,2] = 0.025
  data0[96,3] = 1.93939
  data0[96,4] = 0.0392159
  data0[97,0] = 0.959596
  data0[97,1] = 0
  data0[97,2] = 0.025
  data0[97,3] = 1.9596
  data0[97,4] = 0.0262341
  data0[98,0] = 0.979798
  data0[98,1] = 0
  data0[98,2] = 0.025
  data0[98,3] = 1.9798
  data0[98,4] = 0.0132524
  data0[99,0] = 1
  data0[99,1] = 0
  data0[99,2] = 0.025
  data0[99,3] = 2
  data0[99,4] = 0.000270571
  done=True


