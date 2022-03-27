
import random

alimentos = ["Castanha", "Morango", "Rabanete", "Framboesa", "Pescada", "Leite", "Espinafre", "Coco", "Banana", "Cevada"]
animais = ["Besouro", "Minhoca", "Cabra", "Mula", "Arraia", "Borboleta", "Tatu", "Coelho", "Chita", "Coala"]

list_types = [
    { "alimentos": alimentos },
    { "animais": animais},
]


def list_categories():
    categories = []
    
    for category in list_types:
        category_key = category.keys()
        for item in category_key:
            categories.append(item)
    return categories


def choose_categories(choosed):
    try:
        if choosed.isdigit():
            raise ValueError

        for category in list_types:
            if choosed in category:
                found = category[choosed]
                break

        if len(found): return found


    except TypeError:
        print(" a categoria precisa ser uma das categorias existentes")
    
    except ValueError:
        print("o valor digitado precisa ser uma palavra")


def game(original, scrambled):
    attempts = 3

    while attempts > 0:
        print(f"você deve tentar desembaralhar esta palavra: {scrambled}")
        print(f"tente adivinhar a palavra, você tem {attempts} tentativas")
        player_attempt = input()

        if player_attempt == original:
            print("Parabéns voc6e acertou a palavra")
            break
        
        else:
            attempts -= 1
    
    if attempts == 0:
        print(f"infelismente você perdeu, a palavra era {original}")


def palavras_embaralhadas():
    categories = list_categories()

    list_to_choose = ""
    index = 0

    while index < len(categories):
        list_to_choose += f" {categories[index]},"
        index += 1
    removed_last_comma = list_to_choose.rstrip(list_to_choose[-1])

    print(f"escolha uma categoria: {removed_last_comma}:")
    category_items = choose_categories(input())

    sorted_word = random.choice(category_items)
    scrambled = "".join(random.sample(sorted_word, len(sorted_word)))

    game(sorted_word, scrambled)


palavras_embaralhadas()