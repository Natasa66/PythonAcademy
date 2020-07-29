def leapyear(year):
    if year
        if year % 4 == 0:
            if year % 100 != 0:
                if year % 400:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False

#volanie funkcie
#leapyear(2000)

#volanie funkcie leapyear() v cykle od.....do
rok_od = int(input("Zadaj rok od: "))
rok_do = int(input("Zadaj rok do: "))
for rok in range(rok_od, rok_do+1):  # musim dat +1, lebo for je iba do rok<rok_do
    if leapyear(rok) == True:   #staci if leapyear(rok):     netreba ==True
        print(f"Rok {rok} je prestupny")
    else:
        print(f"Rok {rok} nie je prestupny")