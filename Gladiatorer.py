# Steg 1: Undersök om fienden väljer att använda vapnet eller istället slår eller sparkar
# Steg 2: Om den väljer vapnet, bestäm vilken attack med vapnet den ska göra
# Steg 3: Se om det är en träff eller en miss
# Steg 4: Om det är en miss blir det spelarens tur att anfalla
# Steg 5: Om det är en träff ska spelaren ta skada
# Steg 6: berätta för spelaren vad som händer


import random,msvcrt

print("Du är Gladiatorn Lucius, du ska slåss mot Gladiatorn Gaius")
print("Ni ligger i en romersk arena och är omrigande av publik.")

weapons = ["svärd", "spjut"]
svärdmove = ["hacka", "stabba"]
spjutmove = ["kasta spjut", "spjut droppe"]
luciushp = 100
gaiushp = 100

print("Svärd:\n Hacka\n Stabba")
print("Spjut:\n Spjutdroppe\n Kasta Spjut")

wchoice= input("Vilken vapen vill du välja(Svärd eller Spjut)?").lower()

rundnummer = 1

gaiusw = random.choice(weapons)
if gaiusw == "svärd":
    gaiusmove= random.choice(svärdmove)
elif gaiusw == "spjut":
    gaiusmove= random.choice(spjutmove)

print("Gaius valde vapnet", gaiusw)
if wchoice == "svärd":
    print("Du har vald svärd som vapen.")
elif wchoice == "spjut":
    print("Du valde spjut som vapen.")

print("Din hp är", luciushp,"och motståndarens hp är", gaiushp )

print("Vi börjar med första rundan")

while rundnummer:
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
    
    print("Du väljde", luciusmove, "och Gaius väljde", gaiusmove)

    if luciusmove == "stabba":
        if stabbchance >= 6:
          gaiushp = gaiushp - stabbdamage
    elif luciusmove == "hacka":
        if hackadamage >= 4:
          gaiushp = gaiushp - hackadamage
    elif luciusmove == "kasta spjut":
        if kastchance >=8:
           gaiushp = gaiushp - kastdamage
    elif luciusmove == "spjut droppe":
        if dropchance >= 6:
          gaiushp =  gaiushp - dropdamage
        

    elif luciusmove == gaiusmove:
        print("Ni har valt samma")

    if gaiusmove == "stabba":
        if stabbchance >= 6:
           luciushp = luciushp - stabbdamage
    elif gaiusmove == "hacka":
        if hackadamage >= 4:
          luciushp =  luciushp - hackadamage
    elif gaiusmove == "kasta spjut":
        if kastchance >=8:
           luciushp = luciushp - kastdamage
    elif gaiusmove == "spjut droppe":
        if dropchance >= 6:
           luciushp = luciushp - dropdamage

    print("Din hp är", luciushp,"och motståndarens hp är", gaiushp )
    rundnummer = rundnummer + 1
    print(rundnummer)
    continue
    
        

