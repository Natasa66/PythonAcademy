# vygenerovat zoznam, ktory bude obsahovat 2 mocniny
# [0..10] (range(11))

# zoznam = []
# for i in range(11):
#     zoznam.append(i**2)
# print(zoznam)

if __name__ == __main__:

    zoznam = [i**2 for i in range(11)]
    print(zoznam)


    zoznam_parnych_cisel = [i for i in range(100) if i % 2 == 0]  # tuple,   generator
    print(zoznam_parnych_cisel)

    mena = ["Tomas", "zuzka", "Vierka", "Adam"]
    samohlaska_mena = [
        meno for meno in mena if meno.startswith(("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"))
    ]
    print(samohlaska_mena)