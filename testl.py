import socket
import struct
import time
from hashlib import md5
import sys
import os
import random

t = struct.pack("<H", int(1577364532.1246042) % (0xFFFF))
fo = open("C:\\Users\\70894\\Desktop\\aa.txt", "w")
print("\x01\x02" + "\xe9\x05" + "\x09" + "\x00" * 15)
#fo.write((b'\x01\x02'.decode("utf-8") + t.decode("utf-8") + b'\x09'.decode("utf-8") + (b'\x00' * 15).decode("utf-8")))
#fo.write("\x01\x02" + t + "\x09" + "\x00" * 15)

str = (b'\x01\x02'.decode("utf-8") + t.decode("utf-8") + b'\x09'.decode("utf-8") + (b'\x00' * 15).decode("utf-8"))
s = str.encode("utf-8")
#print(s.decode("utf-8"))
fo.write(str)
fo.close()