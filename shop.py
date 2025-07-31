# this file provides some functions for shop sites

def sum_prod(prod: list[int]) -> int:
    s = sum(prod)
    return s

prices = input("Enter the prices of the products: ").split()
prices = list(map(int, prices))
s_p = sum_prod(prices)
print(f"This is the total price: {s_p}.")

def remove_product(prices, r):
    prices.pop(r-1)
    return prices

def enough_money(s_p):
    i = str(input(f"Do you want to pay {s_p}? y/n "))
    if i == 'y':
        return f"Great! You paid {s_p}."
    elif i == 'n':
        return "Come back later!"
    else:
        return "Error. Invalid input!"
    

rem = input("Do you want to remove some products? y/n ")
print(rem)
if rem == 'y':
    remo = (int(input("Enter the number of the product you want to remove: ")))
    remove_product(prices, remo)
    print("The product has been removed.")
    new_sum = sum_prod(prices)
    print(f"This is new total price: {new_sum}.")
    print(enough_money(new_sum))
elif rem == 'n':
    print("Got it!")
    print(enough_money(s_p))
else:
    print("Error. Invalid input!")
    