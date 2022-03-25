n = 10

last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next


# com fibonacci
number_to_calculate_factorial = 5
value, ant= 1, 1

while value <= number_to_calculate_factorial:
    value, ant = value + 1, value * ant
    print(ant)

# utilizando for para mudar os valores
ratings = [6, 8, 5, 9, 10]

new_note = []

for note in ratings:
    new_note.append(note * 10)

print(new_note)


# utilizando list compreension para mudar os valores
ratings = [6, 8, 5, 9, 10]

new_rating = [note * 10
              for note in ratings
              if type(note) == int ]

print(new_rating)


lista = [1,2,3]

nova_lista = [item + 5
              for item in lista
              if type(item) == int]

print(nova_lista)
