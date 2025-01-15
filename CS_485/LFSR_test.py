import numpy as np
from pylfsr import LFSR

state = [1,1,0,1]
fpoly = [4,2]
L = LFSR(fpoly=fpoly,initstate =state)

# Generate K-bits
k=100
seq_k  = L.runKCycle(k)

print('10 bits')
print(L.arr2str(seq_k))
print('')


# Generate bits of one full period.
# Expected period of LFSR = 2^M-1, for M-bit LFSR).
seq_full  = L.runFullPeriod()

print('Full period of LFSR = 31-cycles')
print(L.arr2str(seq_full))

L.Viz()