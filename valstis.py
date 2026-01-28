import json
import requests
import sqlite3
import os

response = requests.get('https://restcountries.com/v3.1/all?fields=name,population,area,subregion,borders')
#print(response.status_code)
responseParsed = json.loads(response.text)

# if os.path.exists("valstis.db"):
#     os.remove("valstis.db")

con = sqlite3.connect("valstis.db")
cur = con.cursor()



cur.execute("""CREATE TABLE IF NOT EXISTS Valsts(
            ValstsID INTEGER unique primary key,
            Nosaukums varchar(255),
            Platiba integer(255,2))""")

while True:
    ievade = input("Ievadi valsti ko gribi ievadīt:")
    cur.execute(f"""SELECT * from Valsts where Nosaukums="{ievade}" """)
    res = cur.fetchall()
    print("esoshais daudzums:",len(res))
    if ievade == '':
        break
    else:
        for i in responseParsed:
            if (len(res) == 1):
                print("Ir jau bruh")
            else:
                if ievade == i['name']['common']:
                    try:
                        cur.execute(f"""INSERT INTO Valsts(Nosaukums, Platiba) VALUES("{i['name']['common']}","{i['area']}")""")
                        con.commit()
                        print("Valsts pievienota")
                    except:
                        print("Notikusi kļūda, mēginiet vēl reiz")
            continue

con.commit()
con.close()

