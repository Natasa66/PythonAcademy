import random


def vygeneruj_maticu(num_rows, num_columns, min_value, max_value):
    """ Vygeneruje maticu rows x columns s hodnotami min_value .. max_value
    t,j. vygeneruje nahodne cisla od min_value po max_value
          a vypise ich v tvare matice
    :param num_rows: int      # pocet riadkov
    :param num_columns: int    # pocet stlpcov
    :param min_value: int    # minimalna hodnota prvkov v matici
    :param max_value: int    #  maximalna hodnota prvkov v matici
    :return: list (matica rows x columns of int)
    """
    matica = []  # hlavny zoznam - matica - bude to zoznam riadkov matice
    # do tohoto zoznamu budem davat dalsie zoznamy - riadky matice
    if isinstance(num_rows,int) and isinstance(num_columns,int) and isinstance(min_value,int) and isinstance(max_value,int):
        for i in range(num_rows):
            riadok_data = []  #prazdny zoznam, do ktoreho napraskam cisla toho riadku
            # pocet prvkov v riadku je pocet stlpcov!!!!!
            for y in range(num_columns):
                prvok = random.randint(min_value, max_value+1)
                riadok_data.append(prvok)            #pridam do riadku dalsie cislo
            matica.append(riadok_data)
        return matica
    return False

def vytlac_maticu(p_matica, p_riadkov, p_stlpcov)  :
    """
       vytlaci maticu p_riadkov x  p_stlpcov   ako zoznam
    :param p_matica:     list
    :param p_riadkov:     int
    :param p_stlpcov:     int
    :return:
    """
    for i in range(p_riadkov):
        print(p_matica[i])


if __name__ == "__main__":
    pocet_riadkov = int(input("Pocet riadkov: "))
    pocet_stlpcov = int(input("Pocet stlpcov: "))
    minimalna_hodnota = int(input("Zadaj minimalnu hodnotu prvkov: "))
    maximalna_hodnota = int(input("Zadaj maximalnu hodnotu prvkov: "))

    matrix = vygeneruj_maticu(pocet_riadkov, pocet_stlpcov, minimalna_hodnota, maximalna_hodnota)
    vytlac_maticu(matrix,pocet_riadkov,pocet_stlpcov)