import random,msvcrt

print("Du är Gladiatorn Lucius, du ska slåss mot Gladiatorn Gaius")
print("Ni ligger i en romersk arena och är omrigande av publik.")

WChoice= input("Vilken vapen vill du välja(Svärd eller Spjut). Sköld kommer med.")

if WChoice == "svärd":
    print("Du har vald svärd som vapen.")

elif WChoice == "spjut":
    print("Du valde spjut som vapen.")

move = ["spark", "slag", "kast"]

print("Vi börjar med första rundan")
rund1 = 1
while rund1:
    luciusmove=input("Vilket väljer du: slag, spark eller kast")

    slagdamage = random.randint(1,10) 
    slagchance = random.randint(1,10)
    sparkdamage = random.randint(1,10)
    sparkchance = random.randint(1,10) 
    kastdamage = random.randint(1,10)
    kastchance = random.randint(1,10)
    gaiusmove= random.choice(move)

    print("Du väljde", luciusmove, "och Gaius väljde", gaiusmove)

    if luciusmove == "spark":
        
