# this file provides some functions for shop sites

def sum_prod(prod: list[int]) -> int:
    s = sum(prod)
    return f"This is the sum of all products: {s}."

l = input("Enter the prices of the products: ").split()
l = list(map(int, l))
print(sum_prod(l))