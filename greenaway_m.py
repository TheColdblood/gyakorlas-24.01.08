import greenaway_o

def beolvas():
    lista = []
    beFile = open("greenaway.txt", "r", encoding="utf-8")
    #első sor
    beFile.readline()
    #többi sor
    sorok = beFile.readlines()
    for index in range(0, len(sorok), 1):
        tisztitottSor = sorok[index].strip()
        daraboltSor = tisztitottSor.split("-")
        konyvem = greenaway_o.Film(daraboltSor[0], daraboltSor[1])

        lista.append(konyvem)

    return lista

def kiir(lista):
    for index in range(0, len(lista), 1):
        print(lista[index])

def filmekszama(lista):
    print("III/b.")
    print(f"\t A filmek száma: {len(lista)}")

def d(lista):
    print("III/d.")
    talalat =True
    index = 0
    while index < len(lista) or talalat:
        if "szakács" in lista[index].cim.lower():
            talalat = False
        index += 1

    if not talalat:
        print("\t Van olyan film amiben szerepel a  \"szakács\" szó.")
    else:
        print("\t Nincs olyan film amiben szerepel a  \"szakács\" szó.")

