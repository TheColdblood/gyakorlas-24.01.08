def hossz():

    szo1 = input("\t Kérek egy szót: ")
    szo2 = input("\t Kérek egy másik szót: ")

    szo1Hossz = len(szo1)
    szo2Hossz = len(szo2)

    print("I/a.")
    if szo1Hossz > szo2Hossz:
        print(f"\t A hosszabb szó: {szo1}.")
    elif szo2Hossz > szo1Hossz:
        print(f"\t A hosszabb szó: {szo2}.")
    else:
        print("\t Egyenlő hosszúak.")

    print("I/d.")
    kulonbseg = abs(szo1Hossz - szo2Hossz)
    print(f"\t A szavak hosszának a különbsége: {kulonbseg}")
