import subprocess
print("Mac Adresi Değiştiriliyor")
interface=input("Interface Adı:   ")
subprocess.call(["ifconfig",interface,"down"])
yeni_mac=input("Yeni MAC Adresi: ")
subprocess.call(["ifconfig",interface,"hw","ether",yeni_mac])
subprocess.call(["ifconfig",interface,"up"])
print("İşlem Tamam")