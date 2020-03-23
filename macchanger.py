import subprocess
print("Mac Adresi Değiştiriliyor")
print("Changing Mac Address")
interface=input("Interface Name (wlan0 by default):   ") #wifi card to be changed.
subprocess.call(["ifconfig",interface,"down"])
yeni_mac=input("Yeni MAC Adresi (Enter New Mac): ")
subprocess.call(["ifconfig",interface,"hw","ether",yeni_mac])
subprocess.call(["ifconfig",interface,"up"])
