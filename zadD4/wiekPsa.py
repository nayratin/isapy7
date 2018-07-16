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
