parole = "6752"
for i in range(3):
    ievade = input("Ievadi paroli: ")
    if ievade == parole:
        print("Piekļuve atļauta!")
        break
    else:
        print("Nepareiza parole!")
else:
    print("Piekļuve bloķēta!")
