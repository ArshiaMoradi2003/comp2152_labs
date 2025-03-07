import platform
import socket

print("Current")
print(platform.machine())
print("=======================")

print("Current Processor Type")
print(platform.architecture())
print("=======================")

print("Set Socket Timeout to 50 seconds")
print(socket.setdefaulttimeout(50))
print("Set the current Socket Timeout")
print(socket.getdefaulttimeout())

print("======================")
print("")