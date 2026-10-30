summa = 0
skaits = 0
cena = float(input("Ievadi preces cenu: "))
while cena != 0:
    summa += cena
    skaits += 1
    cena = float(input("Ievadi preces cenu: "))
print("Kopējā summa:", round(summa, 2), "EUR")
print("Preču skaits:", skaits)