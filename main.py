print("Automatic order pizza machine. ")
print("Welcome to python pizza deliveries! ")

size = input("What size of pizza do you want? S , M or L. ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
small_pepperoni = 0
medium_pepperoni = 0
large_pepperoni = 0
Total_price = 0

if size == "S":
    print(f"Price = ${small_pizza}")
    if add_pepperoni == "Y":
        small_pepperoni = small_pizza + 2
        print(f"price of small pizza with pepperoni = ${small_pepperoni}")
    if extra_cheese == "Y":
        Total_price = small_pepperoni + 1
        print(f"price with additional cheese = ${Total_price}")
        print(f"Please pay ${Total_price}")
if size == "M":
    print(f"price = ${medium_pizza}")
    if add_pepperoni == "Y":
        medium_pepperoni = medium_pizza + 3
        print(f"price of medium pizza with pepperoni = ${medium_pepperoni}")
    if extra_cheese == "Y":
        Total_price = medium_pepperoni + 1
        print(f"price with additional cheese = ${Total_price}")
        print(f"Please pay ${Total_price}")
if size == "L":
    print(f"price = ${large_pizza}")
    if add_pepperoni == "Y":
        large_pepperoni = large_pizza + 3
        print(f"price of large pizza with pepperoni = ${large_pepperoni}")
    if extra_cheese == "Y":
        Total_price = large_pepperoni + 1
        print(f"Price with additional cheese = ${Total_price} ")
        print(f"Please pay ${Total_price}")
