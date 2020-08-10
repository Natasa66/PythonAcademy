class Ceasar:
    # attributes  - tie alew nahradim moznostou ich vytvorit pri inicializacii cez __init__
    # minimum = 0 #
    # maximum = 26
    # alphabet_length = 26

    def __init__(self, minimum=0, maximum=26, alphabet_lenght=26):  # pociatocne nastavenie
        """
        ****Inicializacia triedy
        :param minimum: int, default 0
        :param maximum: int, default 26
        :param alphabet_lenght:  int, default 26
        """
        self.min = minimum
        self.max = maximum
        self.alphabet_length = alphabet_lenght

        #a viem sem tam dat aj validaciu na vstupy ako v kazdej obycajnej funkcii, napr. z Cezara
        if not isinstance(self.min, int):
            raise  AssertionError("Minimum musi byt int")
        if not isinstance(self.max, int):
            raise AssertionError("Maximum musi byt int")
        if not isinstance(self.alphabet_length, int):
            raise AssertionError("Aphabet_length musi byt int")


    # prepisem si este funkciu na printovanie triedy
    # to je vlastne polymorfizmus - prepiseme vlastnosti "rodicovskej"  triedy
    def __str__(self):
        return f"Minimum: {self.min}, Maximum: {self.max}, APH_LENGTH: {self.alphabet_length}"

    # methods
    def encrypt(self, text, posun):
        """ Vracia retazec sifrovany Cezarovou sifrou
        :param text: str
        :param posun: int
        :return: str
        """
        if not isinstance(text, str):
            return False
        if not isinstance(posun, int) or posun > self.max or posun < self.min:
            return False
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + posun - 65) % self.alphabet_length + 65)
            elif char.islower():
                result += chr((ord(char) + posun - 97) % self.alphabet_length + 97)
            else:
                result += char
        return result

    def decrypt(self, text, posun):
        return self.encrypt(text, 26 - posun)

    def brute_force(self, text):
        """

        :param text:
        :return:
        """
        result = []
        for i in range(26):
            result.append(self.encrypt(text, i + 1))
        return result

# priklad pre triedu - vlastna sifra - ktora zdedi vsetky vlastnost Ceasar a pridam vlastne
class Encryption(Ceasar):
    def own_cipher(self, text):
        result = ''
        for char in text:
            result += char*4
        return result



if __name__ == "__main__":
    #cipher = Ceasar()
    #mozem predefinovat atributy
    #cipher.min = 9
    # ale nerobieva sa to!!!!!
    # v tom pripade si uz ten object vytvorim s inymi atributmi
    #cipher = Ceasar(minimum = 0, maximum = 26, alphabet_length = 26)
    # a samotnej triede tomu vytvorim podmienky tym, ze prepisem __init__ triedy
    # ktora sa inak vytvara automaticky
    cipher = Ceasar(0,26,26)  # attributy nastavujem pri inicializacii
    #pouzitie predefinovanej funkcie na vypisanie objectu
    #tento print zavola uz __str__ predefinovanu v triede Ceasar !!!!
    print(f"Cipher: {cipher}")  # min, min, alphabet_length
    #mozem aj takto
    #cipher = Ceasar()  # nastavi default hodnoty
    encrypted=cipher.encrypt("ab7fkLK)mG")
    decrypted = cipher.decrypt("bcde", 1)
    print(encrypted)
    print(decrypted)
    print(cipher.brute_force("bcde"))
    cipher.__init__()  # znovu mi nainicializuje ten object do pociatocneho stadia

    # tu pouzijem novu triedu so zdedenymi vlastnostami a dalsimi novymi
    own = Encryption()
    print(own.own_cipher("AHOJ"))