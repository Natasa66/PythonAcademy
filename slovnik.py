#tento file obsahuje ukazky ako pracovat s datovymi typmi slovnik
#nie je to hned pouzitelny kod

# dictionary
# dict()
# asociativne_pole

zoznam = []
tuple_ = ()
slovnik = {}

zoznam = [1, 2, 3, 4]
#         0  1  2  3
tuple_ = (1, 2, 3, 4, )
#         0  1  2  3
slovnik = {
    "prvok_1": 1,
    "prvok_2": 2,
    "moje_meno": "Tomas",
    "koordinaty Hlohovca": (123.3423, 2312.423),
    "vnoreny_slovnik": {
        "a": 1,
        "b": 2,
        "dalsi_vnoreny_slovnik": {
            "zoznam": [3, 4, 5, 3]
        }
    }
}

knihkupectvo_tuple_ = (
    ("King", ("Hrbitov zviratek", "osviceni")),
    ("Kukucin", ("Velkou lyzicou", ))
)


knihkupectvo_dict = {
    "king": {"kniha_nazov": "hrbitov zviratek",
             "rok_vydania": 2001},
    "kukucin": {}
}




print(f"PRVOK_2: {slovnik['prvok_2']}")
print(f"Vnoreny_zoznam: {slovnik['vnoreny_slovnik']['dalsi_vnoreny_slovnik']['zoznam'][2]}")
slovnik["novy_kluc"] = {}
slovnik["novy_kluc"]["ahoj_svet"] = "Ahoj, Svet!"
print(slovnik["novy_kluc"])


print(slovnik)

for i in slovnik.items():
    print(f"Kluc: {i[0]} -> Hodnota: {i[1]}")
print("-"*50)

for key, value in slovnik.items():
    print(f"Kluc: {key} -> Hodnota: {value}")

print(f"KEY: {slovnik.keys()}")
print(f"VALUEs: {slovnik.values()}")

print(f"Key: {slovnik['vnoreny_slovnik'].keys()}")