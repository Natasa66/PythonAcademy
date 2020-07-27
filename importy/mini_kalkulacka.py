def spocitaj(cislo1, cislo2) :
    """ Vrati spocitane cisla
    :param cislo1:  int
    :param cislo2:  int
    :return:  int
    """

    if isinstance(cislo1,int) and isinstance(cislo2,int):
        return int(cislo1 + cislo2)
    else:
        return False


if __name__ == "__main__":
    print(spocitaj(2, 6))
    print(spocitaj(5, 2))
    print(spocitaj("kj",6))