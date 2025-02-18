import re

pair_regex = "[A-Z]{3}/[A-Z]{3}"

exchange_rates = {
    "1" :{"currency_pair":"EUR/USD", "exchange_rate":  1.03},
    "2" :{"currency_pair":"EUR/CHY", "exchange_rate": 7.54},
    "3" :{"currency_pair":"EUR/JPY", "exchange_rate":157.26},
}

def show_available_pairs():
    print("AVAILABLE PAIRS:")
    print("0: ADD NEW EXCHANGE RATE")
    for index in exchange_rates:
        print(f"{index}: CURRENCY {exchange_rates[index]["currency_pair"]} | RATE {exchange_rates[index]["exchange_rate"]}")

def add_new_exchange_rate():
    pass

def get_valid_number(mn=0):
    value = None
    while not value:
        try:
            value = float(input("Enter Value:"))
        except ValueError as err:
            print("ENTER A VALID NUMBER!")
            # value = 0
            continue
        
        if value <= mn:
            print(f"VALUE MUST BE >= {mn}!")
            value = None
        else: 
            break
    
    return value


def pair_exists(pair: str):
    for index in exchange_rates:
        if exchange_rates[index]["currency_pair"] == pair:
            return True
    
    return False

def is_pair_valid(pair: str):
    match = re.search(pair_regex, pair)

    return bool(match)


def get_valid_pair():

    pair = None
    print("PAIR FORMAT: EUR/USD, USD/CNY")
    while not pair:
        pair = input("ENTER VALID PAIR:").upper()

        if not is_pair_valid(pair):
            pair = None
        elif pair_exists(pair):
            pair = None
            print("PAIR WAS ALREADY REGISTERED!")
        else: 
            return pair

currency_pair_number = ""

while True:
    show_available_pairs()

    while not currency_pair_number:
        currency_pair_number = input("Currency Pair:")
        if not currency_pair_number in exchange_rates and currency_pair_number != "0":
            print("ENTER A VALID CURRENCY PAIR!")
            currency_pair_number = ""


    if currency_pair_number == "0":
        pair = get_valid_pair()
        ex_rate = get_valid_number()

        exchange_rates[str(len(exchange_rates) + 1)] = {"currency_pair":pair, "exchange_rate":ex_rate}

        currency_pair_number = ""
        value = 0
        continue


    # VALUE: 2

    value = get_valid_number(0)

    rate = exchange_rates[currency_pair_number]["exchange_rate"]

    result = rate * value

    print(f"Result for pair {exchange_rates[currency_pair_number]["currency_pair"]}: {result} \n")

    currency_pair_number = ""
    value = 0
