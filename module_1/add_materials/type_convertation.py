num_1 = str(1)
num_2 = int(1.8)
str_1 = int("3")
print(type(num_1), type(num_2), type(str_1))

volume = float(input("Fuel volume: "))
price = float(input("Fuel price: "))
bill = f"Your bill {volume * price} uah"
print(bill)
print(type(volume), type(price))
