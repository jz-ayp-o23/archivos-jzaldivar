f = open("beatles.txt", encoding="utf8")
for linea in f:
    for caracter in linea:
        print(repr(caracter), end=" ")
    print()
f.close()
