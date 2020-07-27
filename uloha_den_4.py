# 1) Lekcia2/cykly.py
# 	-> v subore je validacia, ci meno zacina samohlaskou
# 	-> vytvorte funkciu, ktora mi vrati True ak meno zacina samohlaskou inak false
#         -> Vytvorte unit-testy (skuste sa zamysliet, co vsetko viem do funkcie zadat a osetrit to)

def zacina_samohlaskou(meno):
    """
    vrati True ak meno zacina samohlaskou inak false
    :param meno: str
    :return: True or False
    """
    if not isinstance(meno,str):
        return False
    samohlasky = ("A", "e", "i", "o", "u", "a", "E", "I", "O", "U")
    if meno[0] in samohlasky:
        return True
    else:
        return False

# Lekcia3/DU/pyramida.py
# 	-> upravte pyramidu tak, aby vystupom z funkcie bol zoznam (list)
#         -> vypiste pyramidu
#         -> upravte volanie na :  if __name__ == "__main__":
#         -> vymyslite unit-testy pre takuto upravenu funkciu
# 		-> bude to nieco podobne ako ta matica


def pyramida(zakladna, orientacia, centrovanie):
    """
    Vykresli pyramidu na zaklade vstupnych parametrov
    :param zakladna:  int [pocet * zakladne pyramidy]
    :param orientacia: str [normalna, obratena]
    :param centrovanie: centrovanie: str [center, left]
    :return: list

    """
    nova_pyramida = []
    if orientacia not in ["normalna", 'obratena']:
        print("Pyramida moze byt iba [normalna] alebo [obratena]")
        return False

    if centrovanie != "center" and centrovanie != "vlavo":
        print("Centrovanie pyramidy moze byt iba [center] alebo [vlavo]")
        return False

    if centrovanie == "center":
        if orientacia == "normalna":

            cislo_riadka = -1
            for i in range(1, zakladna + 1, 2):    #pocet hviezdiciek rastie po 2
                #print(f"{'*' * i:^{zakladna}}")
                cislo_riadka +=1
                riadok = []
                for j in range(cislo_riadka,zakladna//2):       #vyska pyramidy = polovica zakladne
                    riadok.append(" ")            #kolky riadok, tolko medzier vlavo
                for j in range(0, i):
                    riadok.append("*")
                for j in range(cislo_riadka,zakladna//2):        # aj v pravo
                    riadok.append(" ")
                nova_pyramida.append(riadok)
        else:
            cislo_riadka = -1
            for i in range(zakladna, 0, -2):       #pocet hviezdiciek
                #print(f"{'*' * i:^{zakladna}}")
                cislo_riadka +=1
                riadok = []
                for j in range(0,cislo_riadka):
                    riadok.append(" ")
                for j in range(0,i):
                    riadok.append("*")
                for j in range(0,cislo_riadka):
                    riadok.append(" ")
                nova_pyramida.append(riadok)
    else:
        if orientacia == "normalna":
            for i in range(zakladna):
                #print(f"{'*' * (i + 1)}")
                riadok = []
                for j in range(0,i):
                    riadok.append("*")
                nova_pyramida.append(riadok)
        else:
            for i in range(zakladna):
                riadok = []
                #print(f"{'*' * (zakladna - i)}")
                for j in range(zakladna, i, -1):
                    riadok.append("*")
                nova_pyramida.append(riadok)
    return nova_pyramida


if __name__ == "__main__":
    zaklad = int(input("Zadaj velkost zakladne: "))
    orientacia = input("Zadaj orientaciu [normalna, obratena]: ")
    centrovanie = input("Zadaj centrovanie [center, vlavo]: ")

    vysledna_pyramida = pyramida(zaklad, orientacia, centrovanie)
#    print(vysledna_pyramida)
    for i in range(0, len(vysledna_pyramida)):
        print(vysledna_pyramida[i])