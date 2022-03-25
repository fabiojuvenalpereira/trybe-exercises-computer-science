number_list = [5, 5, 10, 5, 5]

def media (numbers):
    result = 0
    for number in numbers:
      result = result + number

    return result / len(numbers)

print(media(number_list))