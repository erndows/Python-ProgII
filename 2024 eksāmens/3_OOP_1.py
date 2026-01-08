class doktori():
    def prog(self):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu:")
        self.skaits = input("Ievadiet doktorāta pacientu skaitu:")
        print(f"Doktorāts {self.nosaukums} apkalpo {self.skaits} pacientus.")

t1 = doktori()
t1.prog()
t2 = doktori()
t2.prog()
