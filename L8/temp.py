import csv

exchange_rates = {
    "1" :{"currency_pair":"EUR/USD", "exchange_rate":  1.03},
    "2" :{"currency_pair":"EUR/CHY", "exchange_rate": 7.54},
    "3" :{"currency_pair":"EUR/JPY", "exchange_rate": 157.26},
    "4" :{"currency_pair":"JPY/EUR", "exchange_rate": 0.0063},
}

file = open("data.csv", "w", newline='\n')

csv_writer = csv.writer(file)

header = ("index", "currency_pair", "exchange_rate",)

csv_writer.writerow(header)

# print(exchange_rates.items())

exchange_rates_tuple = exchange_rates.items()
# dictionary converted into list of tuples
# [('1', {'currency_pair': 'EUR/USD', 'exchange_rate': 1.03}),
#   ('2', {'currency_pair': 'EUR/CHY', 'exchange_rate': 7.54}),
#     ('3', {'currency_pair': 'EUR/JPY', 'exchange_rate': 157.26}),
#       ('4', {'currency_pair': 'JPY/EUR', 'exchange_rate': 0.0063})]

for index, ex_rate in exchange_rates_tuple:
    csv_writer.writerow([index, ex_rate["currency_pair"], ex_rate["exchange_rate"]])

file.close()

file_read = open("data.csv", "r")

csv_reader = csv.reader(file_read)

print(csv_reader)
print(id(csv_reader))

for row in csv_reader:
    print(row)