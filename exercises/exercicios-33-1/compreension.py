# compreension

name_list = [
  { "name": "fabio", "age": 14},
  { "name": "ana", "age": 15},
  { "name": "pedro", "age": 18},
  { "name": "luca", "age": 21},
  { "name": "jose", "age": 34},
  { "name": "joao", "age": 24},
]

child_list = [item
              for item in name_list
              if item["age"] <= 18]

print(child_list)
