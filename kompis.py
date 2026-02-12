import time 
import random

class RAM:
    def __init__(self):
        self.info = "HyperX DDR5 6300 MHz 512 GB"
        self.slegts = False
    
    def Iesledz(self):
        self.slegts == True
    
    def Izsledz(self):
        self.slegts == False

class CPU:
    def __init__(self):
        self.info = "Ryzen 9950X3D 4.3 GHz"
        self.slegts = False
    
    def Iesledz(self):
        self.slegts == True
    
    def Izsledz(self):
        self.slegts == False

class PSU:
    def __init__(self):
        self.info = "LC Power 350 W 80 Plus Bronze"
        self.slegts = False
    
    def Iesledz(self):
        self.slegts == True
    
    def Izsledz(self):
        self.slegts == False

class GPU:
    def __init__(self):
        self.info = "Nvdia RTX 5090 32 GB GDDR7"
        self.slegts = False
    
    def Iesledz(self):
        self.slegts == True
    
    def Izsledz(self):
        self.slegts == False

class Dators:
    def __init__(self):
        self.ram = RAM()
        self.cpu = CPU()
        self.psu = PSU()
        self.gpu = GPU()
        self.saraksts = [self.ram, self.cpu, self.psu, self.gpu]
    def Ieslegt(self):
        while True:
            if random.random() > 0.5:
                for i in self.saraksts:
                    print(i.info)
                    i.Iesledz()
                    print("Ieslēgts")
                break
            else:
                print("Mēģinam atkal!")
                time.sleep(2)
    def Izslegt(self):
        for i in self.saraksts:
            print(i.info)
            i.Izsledz()
            print("Izslēgts")


comp = Dators()
comp.Ieslegt()
comp.Izslegt()