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