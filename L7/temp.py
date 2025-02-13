my_dict = {
    1: {'currency': 'USD/EUR', 'exrate': 0.96 }
}

my_dict[2] = {'currency': 'EUR/USD', 'exrate': 1.0391562678}
my_dict[3] = {'currency': 'USD/JPY', 'exrate':154.22}

print("\nThe current combinations are:\n")

for key, details in my_dict.items():
    print(f"{key}: Currency = {details['currency']}, ExchRate = {details['exrate']}\n")


exchange_rate=0

while True:
  input_value = int(input(f"Please input a value from 1 to {len(my_dict)}: "))
  if input_value in my_dict:
        details = my_dict[input_value]
        print(f"You selected: Currency = {details['currency']}, ExchRate = {details['exrate']}")
        exchange_rate=float(details['exrate'])
        print(type(exchange_rate), exchange_rate)
        break
  else:
        print(f"Invalid input. Please enter a value from 1 to {len(my_dict)}.")

input_amount = float(input("Please input the amount to convert : "))


print("You will receive : " + str(input_amount*exchange_rate))