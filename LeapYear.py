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
