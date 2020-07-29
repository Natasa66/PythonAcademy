#program, ktory zisti, ci zadany rok je prestupny
rok=input("Zadaj rok: ")
rok_int= int(rok)
if rok_int% 4==0:
    if rok_int % 100 != 0:
        if rok_int % 400:
            print(f'Rok {rok_int} je priestupny')
        else:
            print("rok je neprestupny")
    else:
         print("rok je prestupny")
else:
    print(f"Rok {rok_int} nie je priestupny")
#
#pridame rozsah rokov
rok_od = int(input("Zadaj rok od: "))
rok_do = int(input("Zadaj rok do: "))
for rok in range(rok_od, rok_do+1):
    if ((rok%4 == 0) and (rok % 100 != 0)) or rok %400 == 0:
        print(f"Rok {rok} je prestupny")
