from ctypes import cdll

lib = cdll.LoadLibrary("C:\\Users\\Administrator\\source\\repos\\Test1Dll\\x64\\Debug\\Test1Dll.dll")
lib.hello_world()