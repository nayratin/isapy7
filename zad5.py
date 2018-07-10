szerokosc = int(input("Podaj szerokość prostokąta: "))
dlugosc = int(input("Podaj długość prostokąta: "))

podstawa_gorna = "+" + "-" * szerokosc + "+" + "\n"
podstawa_dolna = "+" + "-" * szerokosc + "+"
boki = "|" + " " * szerokosc + "|" + "\n"

print(podstawa_gorna + boki * dlugosc + podstawa_dolna)