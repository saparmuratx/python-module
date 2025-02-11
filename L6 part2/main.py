exchange_rates = {
    "EUR/USD":  1.03,
    "EUR/CHY": 7.54,
    "EUR/JPY":157.26,
}

print(f"AVAILABLE PAIRS: {list(exchange_rates.keys())}")

currency_pair = ""

while not currency_pair:
    currency_pair = input("Currency Pair:")
    if not currency_pair in exchange_rates:
        print("ENTER A VALID CURRENCY PAIR!")
        currency_pair = ""

# VALUE: 2
value = int(input("Enter Value:"))

result = exchange_rates[currency_pair] * value

print(f"Result for pair {currency_pair}: {result}")


