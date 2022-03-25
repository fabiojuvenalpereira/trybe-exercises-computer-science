restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

bests = []
min_rating = 3.0

for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        bests.append(restaurant)

print(bests)
