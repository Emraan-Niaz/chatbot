#!/C:\git\python
# .*. coding: utf-8 -*-

# Ein einfacher ChatBot
# (c) 2020 by me, Lizenz GPLv3

import random
#zufallsantworten = ["Oh wirklich..", "interessant", "Das kann man so sehn", "Ich verstehe..."]
#Stopwörter
reaktionen = {"hallo", "aber hallo",
                "geht", "Was verstehst du darunter"
             }
print ("Wilkommen beim ChatBot  (v1)")
print("Worüber wollen Sie sprechen")
print("Zum Beenden geben Sie bye ein...")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    nutzereingabe = input("Ihre Fragen oder Antwort: ")
    nutzereingabe = nutzereingabe.lower()
    nutzereingabe = nutzereingabe.split()
    for einzelworter in nutzereingabe:
        if einzelworter in reaktionen:
            print(reaktionen[einzelworter])
    #print(random.choice(zufallsantworten))
print("einen schönen Tag.")
