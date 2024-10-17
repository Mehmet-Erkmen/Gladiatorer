import random,msvcrt

print("Du är Gladiatorn Lucius, du ska slåss mot Gladiatorn Gaius")
print("Ni ligger i en romersk arena och är omrigande av publik.")

WChoice= input("Vilken vapen vill du välja(Svärd eller Spjut). Sköld kommer med.")

if WChoice == "svärd":
    print("Du har vald svärd som vapen.")

elif WChoice == "spjut":
    print("Du valde spjut som vapen.")

svärdmove = ["hacka", "stabba"]
spjutmove = ["kasta spjut", "spjut droppe"]
luciushp = 100
gaiushp = 100
gaiusW = random.choices(svärdmove, spjutmove)

print("Vi börjar med första rundan")
rund1 = 1
while rund1:
    if WChoice == "svärd":
        luciusmove = input("Vilken väljer du: Hacka eller stabba? ")
    elif WChoice == "spjut":
        luciusmove = input("Vilken väljer du: Kasta spjut eller spjut droppe? ")
    WChoice = WChoice.lower()

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
    
        

