import ctypes
import time
from numpy.ctypeslib import ndpointer

outputP = (ctypes.c_uint32 * 64000000)()
output = (ctypes.c_uint32 * 64000000)()


start_time = time.time()
for i in range(64000000):
    outputP[i] = outputP[i] + 1

pt = time.time() - start_time
print("--- %s seconds ---" % (pt))
print ("---Python---    ", outputP[999999]*outputP[1999999])

lib = ctypes.CDLL('./library.so')
lib.ls1.argtype = ndpointer(dtype=ctypes.c_int, shape=(64000000,))
lib.ls1.restype = ndpointer(dtype=ctypes.c_int, shape=(64000000,))

start_time = time.time()
res = lib.ls1(output)

ct = time.time() - start_time
print("--- %s seconds ---" % (ct))
print ("---c++---    ", res[999999]*res[1999999])
print ('rate: ', pt/ct)