num = int(input("Podaj liczbę: "))

mess_success= "Twoja liczba jest podzielna przez 3, 5 i 7!"

mess_failed = "Twoja liczba nie dzieli się przez 3, 5 i 7 jednocześnie!"


if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
  print(mess_success)

else:
  print(mess_failed)