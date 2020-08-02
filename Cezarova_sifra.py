import string
import random

def zasifruj_Cezar(retazec:str, posun=0):
    """

    :param retazec: reatzec, ktory sa ma zasifrovat
    :param posun: aky posun ma byt vykonany
    :return: vystypny_retazec
    """
    # skontroluj posun - ak je viac ako 26, tak ho zmensi o nasobky 26
    if posun>=0:
        posun = posun % 26
    else:
        return False

    #inicializacia vystupneho retazca
    vystupny_retazec=""
    # prejdi retazec a posuvaj pismena
    for i in range(0,len(retazec)):
        znak = retazec[i]
        skutocny_posun = 0
        if retazec[i].islower() or retazec[i].isupper():   # ak su to pismena, budem posuvat
            skutocny_posun = posun
            ord_znak = ord(znak)
            if ((ord(znak) + posun) >122) and retazec[i].islower() :
                skutocny_posun = posun - (122 - ord(znak))  - 1  #vypocitam novy posun - od zaciatku abecedy
                znak = 'a'
            elif ((ord(znak) + posun) > 90) and retazec[i].isupper() :
                skutocny_posun = posun - (90 - ord(znak)) - 1 # - 1 -> "dostanem" sa na 'A'
                znak = 'A'

        vystupny_retazec += chr(ord(znak)+skutocny_posun)

    return vystupny_retazec

def rozsifruj_Cezar(retazec:str, posunr=0):
    """

    :param retazec: zasifrovany retazec
    :param posunr:
    :return: vystupny_retazec
    """
    # skontroluj posun - ak je viac ako 26, tak ho zmensi o nasobky 26
    if posunr >=0:
        posunr = posunr % 26
    else:
        return False
    # inicializacia vystupneho retazca
    vystupny_retazec = ""
    # prejdpi retazec a posuvaj pismena
    for i in range(0, len(retazec)):
        znak = retazec[i]
        skutocny_posun = 0
        if retazec[i].islower() or retazec[i].isupper():  # ak su to pismena, budem posuvat
            skutocny_posun = posunr
            if (ord(znak) - posunr) <97 and znak.islower():
                skutocny_posun = posunr - ( ord(znak) - 97) -1 # vypocitam novy posun - od zaciatku abecedy
                znak = 'z'
            elif (ord(znak) - posunr) < 65 and znak.upper():
                skutocny_posun = posunr - (ord(znak) - 65) -1
                znak = 'Z'

        vystupny_retazec += chr(ord(znak)-skutocny_posun)

    return vystupny_retazec

def brutal_force_Cezar(retazec:str):
    """

    :param retazec: retazec, ktory treba rozkodovat
    :return: vsetky mozne povodne retazce
    """
    for i in range(1,27):
        rozsifrovany_retazec=""
        rozsifrovany_retazec = rozsifruj_Cezar(sifrovany_retazec, i)
        print(f"{i} : {rozsifrovany_retazec}")

if __name__ == "__main__":
    vstupny_retazec = str(input("zadaj retazec : "))
    #vstupny_retazec = "BotaS"
    posun = int(input("zadaj posun: "))
    if posun >= 0 and len(vstupny_retazec) > 0:
        sifrovany_retazec = zasifruj_Cezar(vstupny_retazec, posun)
        print("-" * 40)
        print(f"zasifrovany retazec: {sifrovany_retazec}")
        print("-"*40)
        rozsifrovany_retazec=rozsifruj_Cezar(sifrovany_retazec,posun)
        print(f"povodny retazec : {rozsifrovany_retazec}")
        print("-" * 40)
        brutal_force_Cezar(sifrovany_retazec)
        print("koniec filmu")
    else:
        print("nespravne hodnoty na vstupe")