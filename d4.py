# mielismy do zrobienia kalkulator ktory dziala na podstawie decyzji uzzytkowanika w uproszczeniu
def start():
    wybor = input("Wybierz funkcje: ")
    # inputy/
    if wybor == "dodawanie":
        def dodawanie(x = int(input("liczba1")), y = int(input("liczba2"))):
            suma = x + y
            print(suma)
        dodawanie() #inputy; nie mialam wczesniej odwolan funkcji
    elif wybor == "mnozenie":
        def mnozenie(x = int(input("liczba1")), y = int(input("liczba2"))):
            iloczyn = x * y
            print(iloczyn)
    elif wybor == "odejmowanie":
        def odejmowanie(x = int(input("liczba1")), y = int(input("liczba2"))):
            roznica = x - y
            print(roznica)
start() #wywolywalam w princie

