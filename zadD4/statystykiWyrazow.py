chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def letter_stats(yourText):
    for char in chars:
        literka = yourText.count(char)
        print(char + " wystepuje " + str(literka))
#przeliczanie wyrazow dodac

twojText = input("podaj tekst: ")

if twojText.isalnum() == False:
    letter_stats(twojText.lower())
else:
    print("bledy! ponow probe!")
