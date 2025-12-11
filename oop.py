from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards
    @abstractmethod
    def statiesPrieksa(self):
        pass 
        
class Skolens(Persona):
    def __init__(self,vards,uzvards,klase):
        Persona.__init__(self,vards,uzvards)
        self.klase = klase
    def statiesPrieksa(self): 
        print(f"Mani sauc {self.vards} {self.uzvards} un es mācos {self.klase} klasē!")

class Skolotajs(Persona):
    def __init__(self,vards,uzvards,prieksmets):
        Persona.__init__(self,vards,uzvards)
        self.prieksmets = prieksmets
    def statiesPrieksa(self): 
        print(f"Mani sauc {self.vards} {self.uzvards} un es mācu {self.prieksmets}!")
    


p1 = Skolens("Jānis", "Čaugurs", "14.OK")
p2 = Skolens("Plauts", "Maurs", "12.PS")
p3 = Skolens("Cīrliņš", "Kolhevs", "9.a")
s1 = Skolotajs("Bobers","Mihalekovs","Programmēšana V")
s2 = Skolotajs("Miņģels","Duminovs","Fizika -II")
s3 = Skolotajs("Kautris","Jevģijs","Matemātika M")

p1.statiesPrieksa()
p2.statiesPrieksa()
p3.statiesPrieksa()
s1.statiesPrieksa()
s2.statiesPrieksa()
s3.statiesPrieksa()
        


    
