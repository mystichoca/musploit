import subprocess
print("Mac Adresi Değiştiriliyor")
interface=input("Interface Adı:   ")
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["macchanger","--random",interface])
subprocess.call(["ifconfig",interface,"up"])
print("İşlem Tamam")