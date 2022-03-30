import sys
numbers_right = [1, 2, 3, 4]
numbers_wrong = [1, "a", 2, "x"]

def sum_numbers():
    values = input("coloque os números aqui:")
    prev = 0
    error = "not is a number"
    for number in values:
        if type(number) == int: prev += number
        else: return print(f"Error: {error}")

    return print(prev)

sum_numbers()