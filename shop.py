# this file provides some functions for shop sites

def sum_prod(prod: list[int]) -> int:
    s = sum(prod)
    return s

prices = input("Enter the prices of the products: ").split()
prices = list(map(int, prices))
s_p = sum_prod(prices)
print(f"This is the total price: {s_p}.")

def enough_money(s_p):
    i = str(input(f"Do you want to pay {s_p}? y/n "))
    if i == 'y':
        return f"Great! You paid {s_p}."
    elif i == 'n':
        return "Come back later!"
    else:
        return "Error. Invalid input!"
    
print(enough_money(s_p))
