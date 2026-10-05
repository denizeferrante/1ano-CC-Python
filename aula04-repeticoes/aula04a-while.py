cp = 0
while cp < 10:
    cp += 1

    if cp == 3 or cp == 5:
        continue

    if cp == 7:
        break

    print(f"Produto {cp}")

# while decrescente de 4 até 1
i = 4
while i > 0:
    i -= 1
    print(i)