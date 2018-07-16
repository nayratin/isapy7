<<<<<<< HEAD
def dog_age_calc(y):
  """przeliczamy wiek psa zakladajac ze przez pierwsze dwa lata każdy rok to 10.5 lat, a kazdy nastepny to 4"""

  if y > 0 and y <= 2:
    age = 2 * 10.5 + (y - 2) * 4
  else:
    return "niepoprawne dane!"
  print(str(y) + " psich lat to " + str(age) + " ludzkich.")

yoursDogAge = input("Podaj wiek psa: ")

if yoursDogAge.isdigit() == True:
  dog_age_calc(yoursDogAge)
else:
  print("bledne dane! podaj je jeszcze raz!")

=======
def dog_age_calc(y):
  """przeliczamy wiek psa zakladajac ze przez pierwsze dwa lata każdy rok to 10.5 lat, a kazdy nastepny to 4"""
  if y <= 2:
    age = y * 10.5
  elif y > 2:
    age = 2 * 10.5 + (y - 2) * 4
  else:
    pass
  print(str(yoursDogAge) + " psich lat to " + str(age) + " ludzkich.")

yoursDogAge = int(input("Podaj wiek psa: "))

dog_age_calc(yoursDogAge)
>>>>>>> 38a3dbff38094f0c34fc505e4b791aa931ee5bc5
