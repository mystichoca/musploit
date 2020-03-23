import subprocess
print("Monitor Mod Kapatılıyor...")
interface=input("Interface Adı:   ")
subprocess.call(["airmon-ng","stop",interface])
print("Monitor Mod Kapatıldı. Artık Managed Mod'dasınız")