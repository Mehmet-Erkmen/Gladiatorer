# Steg 1: Undersök om fienden väljer att använda vapnet eller istället slår eller sparkar
# Steg 2: Om den väljer vapnet, bestäm vilken attack med vapnet den ska göra
# Steg 3: Se om det är en träff eller en miss
# Steg 4: Om det är en miss blir det spelarens tur att anfalla
# Steg 5: Om det är en träff ska spelaren ta skada
# Steg 6: berätta för spelaren vad som händer


import random,msvcrt

print("Du är Gladiatorn Lucius, du ska slåss mot Gladiatorn Gaius")
print("Ni ligger i en romersk arena och är omrigande av publik.")

wchoice= input("Vilken vapen vill du välja(Svärd eller Spjut). Sköld kommer med.").lower()

if wchoice == "svärd":
    print("Du har vald svärd som vapen.")
elif wchoice == "spjut":
    print("Du valde spjut som vapen.")

weapons = ["svärd", "spjut"]
svärdmove = ["hacka", "stabba"]
spjutmove = ["kasta spjut", "spjut droppe"]
luciushp = 100
gaiushp = 100
gaiusW = random.choice(weapons)
print(gaiusW)

print("Vi börjar med första rundan")
rund1 = 1
while rund1:
    if wchoice == "svärd":
        luciusmove = input("Vilken väljer du: Hacka eller stabba? ")
    elif wchoice == "spjut":
        luciusmove = input("Vilken väljer du: Kasta spjut eller spjut droppe? ")
    wchoice = wchoice.lower()

    hackadamage = random.randint(7,10) 
    hackachance = random.randint(1,10)
    stabbdamage = random.randint(4,8)
    stabbchance = random.randint(1,10) 
    kastdamage = random.randint(3,7)
    kastchance = random.randint(1,10)
    dropdamage = random.randint(4,7)
    dropchance = random.randint(1,10)
    gaiusmove= random.choice(gaiusW)

    print("Du väljde", luciusmove, "och Gaius väljde", gaiusmove)

    if luciusmove == "stabba":
        if stabbchance >= 6:
            gaiushp - stabbdamage
    elif luciusmove == "hacka":
        if hackadamage >= 4:
            gaiushp - hackadamage
    elif luciusmove == "kasta spjut":
        if kastchance >=8:
            gaiushp - kastdamage
    elif luciusmove == "spjut droppe":
        dropchance >= 6

    elif luciusmove == gaiusmove:
        print("Ni har valt samma")
        continue
    
        

