import random
import string

# uloha 1 : vytvor generator nahodneho textu s dlzkou "len"

def generator_nahodneho_textu(len: int):
    if not isinstance(len,int):
        return False
    # string ma "kniznicu"
    required_characters = string.ascii_lowercase+string.ascii_uppercase+string.digits+"?!*."
    #random_text = random.choices(required_characters, k=len) toto vytvori zoznam
    random_text = "".join(random.choices(required_characters,k=len)) #toto mi vytvori text zo zoznamu
    # ['a','b'] -> join => str
    #a b c d -> split => list
    return random_text

# viem to aj uplne sofistikovane v jednom prikaze


# uloha 2 :vytvor funkciu, ktora z lubovolneho textu vytiahne do zoznamu (list)
# #vsetky cisla delitelne dvomi
def vytiahni_cisla_delitelne_dvomi(text_n:str):
    """

    :param text_n: str
    :return: list / False
    """
    if not isinstance(text,str):
        return False

   # dlzka_textu = len(text)
    navrat_zoznam = []
    for znak in text_n:
        if znak.isnumeric() and int(znak) % 2 == 0:
            navrat_zoznam.append(int(znak))

    return navrat_zoznam

# viem to aj cez comprehension
    #navrat_zoznam = [int(znak) for znak in text_n if znak.isnumeric() and int(znak) % 2 == 0]


if __name__ == "__main__":
    dlzka = input("zadaj dlzku retazca ")
    if dlzka.isnumeric():
        dlzka = int(dlzka)
    else:
        dlzka = None
    text = generator_nahodneho_textu((dlzka))
    delitelne_dvomi = vytiahni_cisla_delitelne_dvomi(text)
    print(text)
    print(delitelne_dvomi)

# tento if sa da napisat aj kratsie
# dlzka = int(dlazka) if dlzka.isnumeric() else None