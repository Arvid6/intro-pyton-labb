def recept(antal):
    prod = ["smör", "ströbröd", "ägg", "strösocker", "vaniljsocker", "bakpulver", "vetemjöl", "smör", "vatten"]
    ant1 = [2.5, 0.1875, -1, 0.75, 0.5, 0.5, 0.75, 0.1875, 0.25]
    mot = ["g", "dl", "st", "dl", "tsk", "tsk", "dl", "g", "dl"]
    for (a, b, c) in zip(prod, ant1, mot):
        if a != "ägg":
            b *= antal
        else:
            b += antal
        print(a, b, c)


def tidsblanda(antal):
    return 10 + antal


def tidsgradda(antal):
    return 30 + (3 * antal)


def sockerkaka(antal):
    recept(antal)
    tid1 = tidsblanda(antal)
    tid2 = tidsgradda(antal)
    print(tid1 + tid2, "minuter i ugnen")


def space():
    print()
    print()
    print()


sockerkaka(4)
space()
sockerkaka(7)