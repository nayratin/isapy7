num = int(input("Podaj liczbę: "))

mess_success3= "Twoja liczba jest podzielna przez 3"
mess_success5= "Twoja liczba jest podzielna przez 5"
mess_success7= "Twoja liczba jest podzielna przez 7"
mess_failed = "Twoja liczba nie dzieli się przez 3 lub 5 lub 7!"


if num % 3 == 0:
  print(mess_success3)
elif num % 5 == 0:
  print(mess_success5)
elif num % 7 == 0:
  print(mess_success7)
else:
  print(mess_failed)
