# Användaren får skriva in en variabel "srs" som sedan gämförs med varje variabel i olist (ordlista)
# och när en match hittas skrivs både olist och blist (beskrivningslista) värdet ut för just det ordet.
def srs1(olist, blist):
    for i in olist:
        print(i)
    while True:
        srs = input("Vilket ord vill du söka på?")
        for x, y in zip(olist, blist):
            if x.lower() == srs.lower():  # .lower gör så att det inte spelar någon roll ifall användaren skriver in
                print(x, ": \n", y)  # t.ex ord/ORD/Ord för alla variabler gämförs som #lowercase tack vare .lower()
                return 0
        print("Ordet finns inte")


# Användaren skriver först in ordet följt av beskrivningen och båda läggs till i slutet av respektive lista med .append
def leg1(olist, blist):
    x = input("Vilket ord vill du lägga till?")
    for i in olist:
        if i.lower() == x.lower():
            print("Ordet finns redan")
            return 0
    y = input("Vad betyder ordet?")
    olist.append(x)
    blist.append(y)
    print("Ordet lades till")


# Två listor skapas som inehåller ord och beskrivningar, Sedan får användaren skriva in Söka,
# Lägga eller Avsluta för att gå vidare,
def ordlista1():
    olist = ["Smör"]
    blist = ["Populärt pålägg på bröd"]
    while True:
        x = input("Vad vill du göra? Vill du LÄGGA till ord, SÖKA ord eller AVSLUTA")
        if x.lower() == "söka":
            srs1(olist, blist)
        if x.lower() == "lägga":
            leg1(olist, blist)
        if x.lower() == "avsluta":
            return 0


# Liknande som första srs, användaren skiver in ett ord och den gärmför ordet med det första elementet i varje tuple,
# när den sedan hittar en matching så skriver den ut både första och andra elementet i tuplen som matchade
def srs2(listan):
    for x in listan:
        print(x[0])
    while True:
        srs = input("Vilket ord vill du söka på?")
        for i in listan:
            if i[0].lower() == srs.lower():  # [0] efter i representerar det första elementet i varje tuple som listan
                # inehåller
                print(i[0], ": \n", i[1])
                return 0
        print("Ordet finns inte")


# Samma som leg2 fast nu läggs båda variablerna in i listan i from av en tuple
def leg2(listan):
        x = input("Vilket ord vill du lägga till?")
        for i in listan:
            if i[0].lower() == x.lower():
                print("Ordet finns redan")
                return 0
        y = input("Vad betyder ordet?")
        listan.append((x, y))
        print("Ordet lades till")


# Exakt samma som ordlista1 förutom att det skapas en lista istället för två
def ordlista2():
    listan = [("Hej", "en hälsning")]
    while True:
        x = input("Vad vill du göra? Vill du LÄGGA till ord, SÖKA ord eller AVSLUTA")
        if x.lower() == "söka":
            srs2(listan)
        if x.lower() == "lägga":
            leg2(listan)
        if x.lower() == "avsluta":
            return 0


# Användaren får åter igen skriva in ett ord och ett if statment kollar om ordet finns på listan, om det inte finns får
# användaren skriva in ett nytt ord och om det finns skrivs det ut
def srs3(listan):
    for x in listan:
        print(x)
    while True:
        srs = input("Vilket ord vill du söka på?")
        if not listan.get(srs):
            print("Ordet finns inte")
        else:
            print(listan.get(srs))
            return 0


# Samma som leg1 och 2 men variablerna lägs till i listan genom listan[x] = y istället för append eftersom det är en
# annan typ av variabel
def leg3(listan):
    x = input("Vilket ord vill du lägga till?")
    if listan.get(x):
        print("Ordes finns redan")
        return 0
    y = input("Vad betyder ordet?")
    listan[x] = y
    print("Ordet lades till")
    return 0


# Samma som ordlista1 och 2 förutom att programmet deklarerar en dictionary istället för en lista.
def ordlista3():
    listan = {
        "Grodor": "små grodorna är lustiga"
    }
    while True:
        x = input("Vad vill du göra? Vill du LÄGGA till ord, SÖKA ord eller AVSLUTA")
        if x.lower() == "söka":
            srs3(listan)
        if x.lower() == "lägga":
            leg3(listan)
        if x.lower() == "avsluta":
            return 0


while True:
    s = input("1, 2 eller 3")
    if s == "1":
        ordlista1()
    if s == "2":
        ordlista2()
    if s == "3":
        ordlista3()
