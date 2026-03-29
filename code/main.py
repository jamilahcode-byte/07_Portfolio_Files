import ctypes

lib = ctypes.CDLL("/storage/emulated/0/libadd.so")  # full path works
print(lib.add(2,3))