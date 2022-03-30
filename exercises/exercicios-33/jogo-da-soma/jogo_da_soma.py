import random

def counter():
    value = 0
    sorted = round(random.randint(0,100))
    print("Você deverá acertar qual é o número secreto, entre 0 e 100.")
    print("Você só poderá acrescentar valores, e estes são: 2, 3 ou 5.")
    print("caso digite algum valor diferente, ele arredondará para o mais próximo equivalente do jogo.")
    print("caso apareça a mensagem: 'tá quase!', significa que você pode estar até 10 números do número secreto")
    print("boa sorte!!!")

    while value < sorted:

        if value == 0:
            value_in = int(input("digite um numero: "))

            if value_in >= 5: value_in = 5
            elif value_in < 5 and value_in >= 3 : value_in= 3
            elif value_in < 3 and value_in >= 1 : value_in= 2
            else: value_in = 0

            value += value_in

        else:
            print("valor atual", value)
            value_in = int(input("digite mais um numero: "))

            if value_in >= 5: value_in = 5
            elif value_in < 5 and value_in >= 3 : value_in= 3
            elif value_in < 3 and value_in >= 1 : value_in= 2
            else: value_in = 0

            value += value_in

            if value + 10 >= sorted: print("tá quase!")

    if value == sorted: print("parabéns, você ganhou!! O numero sorteado era:", sorted)
    else: print("Estourou com:", value, "o valor correto era:", sorted)

counter()