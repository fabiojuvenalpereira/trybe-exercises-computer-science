# imc calc
def imc (peso, altura):
    message = ""

    imc_pessoa = peso / (altura /100) ** 2

    if 18.5 < imc_pessoa < 24.9: message = "pesso muito baixo"
    elif  25 < imc_pessoa < 29.9: message = "normal"
    elif  30 < imc_pessoa < 34.9: message = "acima do peso"
    elif  35 < imc_pessoa < 39.9: message = "gordo"
    else: message = "gordão pra caralho"

    return message, imc_pessoa

print(imc(90, 180))

def pao_por_pessoa (qtd):
    return qtd * 10


# calculadora
def calculadora (first, second, mode):
    result = 0

    if mode == "sum":
        result = first + second

    elif mode == "min":
        if first > second: result = first - second
        elif second > first: result = second - first

    elif mode == "mult":
        result = first * second

    else:
        if first > second: result = first / second
        elif second > first: result = second / first

    return result


print(calculadora(5,10, "mult"))