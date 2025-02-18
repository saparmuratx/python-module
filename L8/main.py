import re
import csv

pair_regex = "[A-Z]{3}/[A-Z]{3}"

def read_exchange_rates():
    res = dict()

    with open("data.csv", "r") as data_file:
        csv_reader = csv.reader(data_file)

        next(csv_reader)

        for row in csv_reader:
            index, pair, rate = tuple(row)
            res[index] = {'currency_pair': pair, 'exchange_rate': float(rate)}

        return res


def write_exchange_rate(key, pair, rate):
    with open("data.csv", "a", newline='') as data_file:
        csv_writer = csv.writer(data_file)

        csv_writer.writerow([key, pair, rate])

    var = 0

    def inline_function():

        pass
    

exchange_rates = read_exchange_rates()

def show_available_pairs():
    print("AVAILABLE PAIRS:")
    print("0: ADD NEW EXCHANGE RATE")
    for index in exchange_rates:
        print(f"{index}: CURRENCY {exchange_rates[index]["currency_pair"]} | RATE {exchange_rates[index]["exchange_rate"]}")
    print("X: TO EXIT")


def get_valid_number(mn=0):
    value = None
    while not value:
        try:
            value = float(input("Enter Value:"))
        except ValueError as err:
            print("ENTER A VALID NUMBER!")
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

        if currency_pair_number.upper() == 'X':
            print("EXITED WITH GRACE")
            exit()

        if not currency_pair_number in exchange_rates and currency_pair_number != "0":
            print("ENTER A VALID CURRENCY PAIR!")
            currency_pair_number = ""


    if currency_pair_number == "0":
        pair = get_valid_pair()
        ex_rate = get_valid_number()
        key = str(len(exchange_rates) + 1)

        exchange_rates[key] = {"currency_pair":pair, "exchange_rate":ex_rate}
        
        write_exchange_rate(key, pair, ex_rate)

        currency_pair_number = ""
        value = 0
        continue

    value = get_valid_number(0)

    rate = exchange_rates[currency_pair_number]["exchange_rate"]

    result = rate * value

    print(f"Result for pair {exchange_rates[currency_pair_number]["currency_pair"]}: {result:.3f} \n")

    currency_pair_number = ""
    value = 0
