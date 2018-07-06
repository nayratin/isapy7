num = int(input("Podaj liczbę: "))

mess_success = "Twoja liczba jest parzysta"
mess_failed = "Twoja liczba jest nieparzysta"


if num % 2 == 0:
  print(mess_success)
elif num % 2 == 1:
  print(mess_failed)
