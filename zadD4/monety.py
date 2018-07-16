coins = [5, 2, 1, 0.50, 0.20, 0.10]

def money_exchange(m):
    for coin in coins:
        coinAmount = m // coin
        m = m % coin
        print("ilosc: " + str(coinAmount) + " monet o nominale " + str(coin))

money = float(input("Podaj kwote: "))

money_exchange(money)

