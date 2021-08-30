def add(li, listan):
    if listan.get(li[1]):  # if/elif statement som kollar om namn eller siffran är definerad sen innan
        print("Namnet finns redan")
    elif li[2] in listan.values():
        print("Siffran finns redan")
    else:
        listan[li[1]] = li[2]


def lookup(li, listan):
    if listan.get(li[1]):
        print(listan.get(li[1]))
    else:
        print("Namnet finns inte")


def alias(li, listan):
    if listan.get(li[2]):
        print("Namnet finns redan")
    elif listan.get(li[1]):
        listan[li[2]] = listan[li[1]]  # Skapar ett alias genom ge den nya keyn samma value som dens alias
    else:
        print("Namnet finns inte")


def change(li, listan):
    if li[2] in listan.values():
        print("Siffran finns redan")

    elif listan.get(li[1]):
        teplist = []  # Skapar en temporär lista
        for x in listan:  # Går igenom alla keys i listan och lägger till alla element som delar value
            # med keyn man vill ändra i teplist
            if listan[x] == listan[li[1]]:
                teplist.append(x)
        for x in teplist:  # Ändrar alla talen i teplist till det nya numret, använder två for-loopar för att
            # inte skapa problem när ett nummer ändras innan resten av numrena som ska ändras kan gämföras
            listan[x] = li[2]
    else:
        print("Namnet finns inte")


def save(li, listan):
    f = open(li[1] + '.txt', "w")
    for x in listan:  # Sparar dictonaryn i en .txt fil som value;key;
        f.write(str(listan[x]))
        f.write(";")
        f.write(str(x))
        f.write(";\n")
    f.close()


def load(li, listan):
    listan.clear()  # rensar dictionaryn
    with open(li[1] + ".txt") as f:
        for x in f:
            lo = list(x.split(";"))  # splitar .txt filen in i en array och använder ; för att skilja mellan orden
            listan[lo[1]] = lo[0]  # lägger till varje key och value i dictionaryn


def Telefonbok():
    listan = {

    }
    while True:
        x = input("Vad vill du göra?")
        li = list(x.split())  # Splitar det användaren skriver in i delar så koden kan läsa det
        if li[0].lower() == "add":
            add(li, listan)
        if li[0].lower() == "lookup":
            lookup(li, listan)
        if li[0].lower() == "alias":
            alias(li, listan)
        if li[0].lower() == "change":
            change(li, listan)
        if li[0].lower() == "save":
            save(li, listan)
        if li[0].lower() == "load":
            load(li, listan)
        if li[0].lower() == "quit":
            print("hejdå")
            break  # avslutar programmet genom att avsluta while-loopen


Telefonbok()
