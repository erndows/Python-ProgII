class Gramata:
    def __init__(self,autors,nosaukums,zanrs):
        self.autors = autors
        self.nosaukums = nosaukums
        self.zanrs = zanrs
    def __str__(self):
        return f"{self.autors}, {self.nosaukums}, {self.zanrs}"


class Biblioteka:
    def __init__(self):
        self.gramata = Gramata("Burnis Humors","Jaunie komunisti","Manifests")
        self.gramata1 = Gramata("Džordžš Orvels","Dzīvnieku ferma","Satīra novele")
        self.gramata2 = Gramata("Džordžš Orvels","1984","Distopiska Literatūra")
        self.gramata3 = Gramata("Jana Egle","Svešie jeb miļenkij ti moj","Stāstu Krājums")
        self.gramata4 = Gramata("Jānis Berdis", "Pazīstamie", "Nākotnes Literatūra")
        self.gramata5 = Gramata("Klaniņš Burbis", "Burbis: Autobiogrāfija","Autobiogrāfija")
        self.saraksts = [self.gramata,self.gramata1, self.gramata2, self.gramata3, self.gramata4, self.gramata5]


    def VisApskate(self):
        for i in self.saraksts:
            print(i)

    def Atrast(self):
        self.izvele = input("Kuru grāmatu vēlaties?(Pēc nosaukuma):")
        for i in self.saraksts:
            if self.izvele == i.nosaukums:
                print(f"{i} atrasta")
    
    def Iznemt(self):
        self.iznemtIzv = input("Kuru grāmatu vēlaties izņemt?(Pēc nosaukuma):")
        for i in self.saraksts:
            if self.iznemtIzv == i.nosaukums:
                print(f"{i} ir izņemta")
                self.saraksts.remove(i)
        for i in self.saraksts:
            print(i)
                
                

bib = Biblioteka()
bib.VisApskate()
bib.Atrast()
bib.Iznemt()

        


