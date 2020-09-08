""" Trieda zaoberajuca sa pracou so slovenskymi rodnymi cislami
"""
import datetime
import random


class BirthNumber:
    """ Praca s rodnymi cislami """
    def __init__(self, birth_number):
        """ Inicializacia rodneho cisla
        :param birth_number:
        """
        if isinstance(birth_number, str):
            self.birth_number = birth_number.replace("/", "") #vsetky lomitka som nahradila "nicim"
        else:
            raise TypeError("Birth number must be string")

    def validate_rc(self):
        """ Validuje, ci je rodne cislo platne
        Ak je človek narodený pred 1.1.1954 má 9 ciferné rodné číslo (3 číslice za lomítkom)
          a číslo nemusí byť deliteľné 11
        Ak je človek narodený po 31.12.1953 má 10 ciferné rodné číslo
          a číslo musí byť bezo zvyšku deliteľné 11 (4 cislice za lomítkom)
        Ženy majú druhé dvojčíslie začínajúce na 5, respektíve 6 (muži 0 a 1)
            830202 vs 835202
            831202 vs 836202
        """
        # prve najrychlejsie je, ci je rodne cislo 10 alebo 9 znakov,ak 9 som ok,
        # ak 10, musi byt delitelne 11
        if len(self.birth_number) == 9 or (len(self.birth_number) == 10 and int(self.birth_number) % 11 == 0):
            # ak prejdem touto validaciou, musim overit, ze prvych 6 znakov je platny datum!
            rc_tmp = int(self.birth_number)
            if self.birth_number[2] == '5' or self.birth_number[2] == '6': #je to zena
                rc_tmp -= 50000000  #51/62  vs  01/12  t.j. mesiac si upravim na taky, aky realny ma byt
            # upravil som si rc na normalny tvar, nezavisle na pohlavi
            rc_tmp = str(rc_tmp)
        else:
            return False
        # vyberiem si prvych 6 znakov a potrebujem overit, ci je to datum
        check_date = rc_tmp[:6]
        #000101 -> 1.1.2000
        #  --  >  01 - 12    mesiac
        #  --  > februar -> 1-29, a 30-dnove mesiace , 31-dnove mesiace
        # mozeme na to vytvorit sadu testov
        #alebo vyuzit Python kniznice:
        try:
            # skusime prvych 6 znakov previest na datum, %y%m%d vravi, ze vkladame YYMMDD format
            datetime.datetime.strptime(check_date, "%y%m%d")  #urob mi datum zo stringu podla toho kluca
            # je to funkcia, ktora vracia rok, takze ak by sme s tym chceli pracobvat dalej
            # tak pridelime vysledok do premennej :
            # premenna_year = datetime.datetime.strptime(check_date, "%y%m%d")
        except ValueError:
            # ak dostaneme valueerror => nieje mozne spravit z retazca datum -> nie je to datum
            return False
        return True

    def get_birth_date(self):
        """ Vrati mi datum narodenia. Format:  DD.MM.YYYY
        napr:  10.10.1010
        Samozrejme iba v pripade, ze rodne cislo je platne!
        """
        if self.validate_rc():
            return datetime.datetime.strptime(self.birth_number[:6], "%y%m%d").strftime("%d.%m.%Y")
        # [:6} - odsekne prvych 6 znakov, t.j. datum narodenia
        #strftime urobi z datumu retazec a naformatuje ho podla kluca, ktoy mu poslem ako argument

    def get_age(self):
        """ Vrati vek cloveka definovaneho rodnym cislom
        """
        today = datetime.date.today()
        born = datetime.datetime.strptime(self.birth_number[:6], "%y%m%d")
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        # porovnava sa rok a este ci dnesny den je "mensi" ako den a mesiac narodenia
        # vysledok porovnavania ak je 1, tak este to odratam od veku - roku
    # napr. dnes je 10.8.2020 a ten clove sa narodil 12.11.1923 , t.j. tento rok este nemal narodeniny
    # a jeho vek bude 2020-1923-1

    def generate_bn(self, birth_date, sex):
        """ Bonusová úloha: generator rodneho cisla definovaneho datumom narodenia
        :param birth_date: dátum narodenia v tvare  DD.MM.YYYY (1.1.2000)
        :param sex: pohlavie  male/female
        :return:
        """
        if sex not in ['male', 'female']:
            raise AttributeError("Pohlavie (sex) moze byt iba male/female")
        birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y")  #DD.MM.YYYY
        bn = birth_date.strftime("%y%m%d")
        # ak je to zena... tak pripocitam 5 k 2hemu miestu
        bn = bn if sex == "male" else bn[:2] + str(int(bn[2]) + 5) + bn[3:]
        #retazec si musim nasekat a znovu pospajat, inak to neupravim pre zenu - retazce su unmutable
        #bn - birth number = datum nar.napr. 101220 / dopocitat stvorcislie za lomitkom
        # bn[:2]> 01
        #bn[2] -> 1 alebo 6    ak zena int(bn[2])+5    01 -> 51   10 -> 60
        #bn[:3] -> 0  10
        # ale uplne staci k tomu priratat tych 50000000 naaspat  :-)

        res = str(bn) + str(random.randint(1000, 9999))
        if birth_date.year < 1954:
            bn += str(random.randint(100, 999))
            return bn
        while int(res) % 11 != 0:
            # generujem nahodne 4 cislie, az kym to cele neni delitelne 11
            res = str(bn) + str(random.randint(1000, 9999))
        return res