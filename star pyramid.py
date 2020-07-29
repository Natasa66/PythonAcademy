#
print("Najprv cez for")
for i in range(10):
    # i bude od 0 po 9, teda ho vzdy musim zvysit o 1
    print("*"*(i+1))
print("-"*20)
#obratena pyramida
for i in range(10):
    print( "*"*(10-i))
# alebo dame range zostupne
# for i in range(10,0,-1):   # t.j. od 10, po 0, step -1
#    print("*"*i)
#


# teraz cez while
print("Teraz cez while.\n")
print("-"*40)
i=1
while i<=10:
    print("*"*i)
    i=i+1
print("-"*20)
i=10
#obratena pyramida
while i>0:
    print("*"*i)
    i=i-1
#vycentrovana pyramida
print("-"*15,"vycentrovana","-"*15)
i=1
odskok=0
while i<10:
    print(" "*(4-odskok),"*"*i)
    i=i+2
    odskok=odskok+1
# odskok nepotrebujem ak pouzijem formatovany print
# print(f'{"*"*i:^15}')  - toto to vycentruje na 15 znakov
#potom staci:
# for i in range(1,16,2,):   # od 1 do 16 step 2,t.j. [1,3,5,7,9,11,13,15]
#    print(f'{"*"*i}^15')  # jedina nevyhoda, moze tam byt maximalne 15 hviezdiciek
#

i=9
odskok=0
while i>0:
    print(" "*odskok,"*"*i)
    i=i-2
    odskok=odskok+1
print("Koniec")