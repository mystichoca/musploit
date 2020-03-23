import subprocess
interface=input("Interface Adı: ")
print(interface" Monitor Mod'a Alınıyor")
subprocess.call(["airmon-ng","start",interface])

print(interface," Monitor Mod'a Alındı.")