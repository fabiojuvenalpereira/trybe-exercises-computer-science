
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


def select_category(categories):
    list_to_choose = ""
    index = 0

    while index < len(categories):
        list_to_choose += f" {categories[index]},"
        index += 1
    removed_last_comma = list_to_choose.rstrip(list_to_choose[-1])

    print(f"escolha uma categoria: {removed_last_comma}:")
    category_items = choose_categories(input())
    
    return category_items


def game(original, scrambled):
    attempts = 3

    while attempts > 0:
        print(f"Você deve tentar adivinhar qual é esta palavra: {scrambled}.")
        print(f"Você ainda possui {attempts} tentativas!")
        player_attempt = input()

        if player_attempt.upper() == original.upper():
            print("Parabéns você acertou a palavra")
            break
        
        else:
            attempts -= 1
    
    if attempts == 0:
        print(f"Infelismente não foi desta vez, a palavra era {original}.")


def palavras_embaralhadas():
    categories = list_categories()
    
    category_items = select_category(categories)

    sorted_word = random.choice(category_items)
    scrambled = "".join(random.sample(sorted_word, len(sorted_word)))

    game(sorted_word, scrambled)


palavras_embaralhadas()