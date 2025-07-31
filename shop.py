# this file provides some functions for shop sites

def sum_prod(prod: list[int]) -> int:
    s = sum(prod)
    return f"This is the sum of all products: {s}."

prices = input("Enter the prices of the products: ").split()
prices = list(map(int, prices))
print(sum_prod(prices))