class Skolotajs():
        stunSkaits = 0
        tips = 1
        uzvards = ""
        

class SakumskolasSkolotajs(Skolotajs):
    def __init__(self):
        self.uzvards = input("Ievadiet sākumskola skolotāja uzvārdu: ")
        self.klase = input("Ievadiet skolotāja klasi: ")
        self.stunSkaits = input("Ievadiet skolotāja stundu skaitu: ")
    def izvade(self):
        self.tips = 1
        print(f"Sākumskolas (tips - {self.tips}) skolotājs {self.uzvards} māca {self.stunSkaits} stundas {self.klase} klasē ")


class VidusskolasSkolotajs(Skolotajs):
    def __init__(self):
        self.uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
        self.pirmais = input("Ievadiet pirmo pasniegto priekšmetu:")
        self.pirmaisSk = int(input("Ievadiet pirmā priekšmeta stundu skaitu:"))
        self.otrais = input("Ievadiet otro pasniegto priekšmetu:")
        self.otraisSk = int(input("Ievadiet otrā priekšmeta stundu skaitu:"))
        
    def izvade(self):
        self.tips = 3
        self.stunSkaits = self.pirmaisSk + self.otraisSk
        print(f"Vidusskolas (tips - {self.tips}) skolotājs {self.uzvards} māca šadus priekšmetus:{self.pirmais} un {self.otrais}, kopā {self.stunSkaits}")

s1 = SakumskolasSkolotajs()
s2 = VidusskolasSkolotajs()

s1.izvade()
s2.izvade()