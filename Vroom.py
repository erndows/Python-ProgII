import random
import keyboard
import time
import webbrowser

print("Ātrs un bez garantijas. 12ID brauciens!")

class Auto:
    def __init__(self,modelis,gads):
        self.modelis = modelis
        self.gads = gads
        self.atrums = 0
        self.iedarbinats = False
    def Start(self):
        if self.iedarbinats == False:
            self.iedarbinats = True
            print("Mašīna iedarbināta!")
    def Paatrinajums(self):
        if self.iedarbinats == True:
            self.atrums += random.randint(1,5)


cipar = [3,2,1]
vroomer = Auto(input("Ievadiet savas mašīnas modeli:"),input("No kura gada šī mašīna: "))
evilVroomer = Auto(input("Ievadiet pretinieka mašīnas modeli:"),input("No kura gada šī mašīna: "))
print("Spiediet s lai sāktu")
keyboard.wait('s')
print("Sveicināti uz ""Ātrs un bez garantijas"", lai spēlētu tikai vajag enter pogu")
time.sleep(3)
print(f"Tavs auto: {vroomer.modelis} ({vroomer.gads})")
time.sleep(2)
print(f"Pretinieka auto: {evilVroomer.modelis}({evilVroomer.gads})")
time.sleep(2)
print("Iedarbiniet auto! (spiediet 1 lai iedarbinātu)")
keyboard.wait('1')
vroomer.Start()
evilVroomer.Start()
print("Gatavojies!")
time.sleep(3)
for i in cipar:
    print(f"{i}...")
    time.sleep(1)
print("Spied 'Enter' lai uzņemtu ātrumu!")
excluded_key = 'Enter'
while True:
    keyboard.wait(excluded_key)
    vroomer.Paatrinajums()
    evilVroomer.Paatrinajums()
    print(f"Spēlētājs:{vroomer.atrums} km/h Pretinieks:{evilVroomer.atrums} km/h")
    if vroomer.atrums >= 100:
        print("Spēlētājs uzvar!")
    elif evilVroomer.atrums >= 100:
        print("Pretinieks uzvar!")
        break
    # event = keyboard.read_event()
    # if event.event_type != keyboard.KEY_DOWN(excluded_key):
    #     print("tu avarēji")
    #     webbrowser.open('https://www.youtube.com/watch?v=RgKAFK5djSk')
    #     break
            
                

        

        