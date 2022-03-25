def square(number):
    caractere = "[*]"
    initial = 0

    while initial < number:
        print(caractere * number)
        initial += 1


square(25)