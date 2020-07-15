#
print("Najprv cez for")
for i in range(10):
    # i bude od 0 po 9, teda ho vzdy musim zvysit o 1
    print("*"*(i+1))
print("-"*20)
for i in range(10):
    print( "*"*(10-i))
# teraz cez while
print("Teraz cez while.\n")
print("-"*40)
i=1
while i<=10:
    print("*"*i)
    i=i+1
print("-"*20)
i=10
while i>0:
    print("*"*i)
    i=i-1
print("Koniec")