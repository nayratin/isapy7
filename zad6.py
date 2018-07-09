binarna = input("Podaj liczbê zapisan¹ w systemie binarnym o d³ugoœci 6 znaków: ")

if len(binarna) == 6:
  dziesietna = 2 ** 5 * int(binarna[0]) + 2 ** 4 * int(binarna[1]) + 2 ** 3 * int(binarna[2]) + 2 ** 2 * int(binarna[3]) + + 2 ** 1 * int(binarna[4]) + 2 ** 0 * int(binarna[5])
  print(str(binarna) + " to " + str(dziesietna) + ".")
else:
  print("Twoja liczba jest za niepoprawnej d³ugoœci!")