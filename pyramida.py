#vytvorte funkciu, ktorej vstupom bude pocet hviezdiciek zakladne a vykreslite
#pomocou nej obratenu pyramidu

def obratena_pyramida(num_stars):
    """vykreslenie obratenej pyramidy

    :param num_stars: int - pocet hviezdiciek v prvom riadku
    :return: none
    """
    if num_stars:
        for i in range(num_stars, 0, -1):
            print(f"{'*'*i}")
    else:
        print("nezadali ste pocet hviezdiciek")

# ideme ju zavolat
# teraz je to znefunkcnene, lebo vytvorim vseobecnejsiu funkciu na pyramidu
#pocet_hviezd=int(input("Zadaj pocet hviezd: "))
#obratena_pyramida(pocet_hviezd)

# vytvorte funkciu, ktora vykresli pyramidu na zaklade vstupnych parametrov
def pyramida(zakladna, orientacia, centrovanie):
    """
    Vykresli pyramidu na zaklade vstupnych parametrov
    :param zakladna:  int [pocet * zakladne pyramidy]
    :param orientacia: str [normalna, obratena]
    :param centrovanie: centrovanie: str [center, left]
    :return: None
    
    """
    if orientacia != ["normalna", 'obratena']:
        print("Pyramida moze byt iba [normalna] alebo [obratena]")
        return False
        # raise NotImplementedError("Pyramida moze byt iba [normalna] alebo [obratena]")
    if centrovanie != "center" and centrovanie != "vlavo":
        print("Centrovanie pyramidy moze byt iba [center] alebo [vlavo]")
        return False
        # raise NotImplementedError("Centrovanie pyramidy moze byt iba [center] alebo [vlavo]")

    if centrovanie == "center":
        if orientacia == "normalna":
            for i in range(1, zakladna + 1, 2):
                print(f"{'*' * i:^{zakladna}}")
        else:
            for i in range(zakladna, 0, -2):
                print(f"{'*' * i:^{zakladna}}")
    else:
        if orientacia == "normalna":
            for i in range(zakladna):
                print(f"{'*' * (i + 1)}")
        else:
            for i in range(zakladna):
                print(f"{'*' * (zakladna - i)}")
    return None
    # return ["*", "**", "***"]
    # return "*\n**\n***"

zaklad = int(input("Zadaj velkost zakladne: "))
orientacia = input("Zadaj orientaciu [normalna, obratena]: ")
centrovanie = input("Zadaj centrovanie [center, vlavo]: ")

design_pyramida = pyramida(zaklad, orientacia, centrovanie)
print(design_pyramida)   # None