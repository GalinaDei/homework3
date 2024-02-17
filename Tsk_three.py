# Задание 3:
# ✔ Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.
import itertools

MAX_WEIGHT = 18000
list_of_things = {"rubber boots": 1000, "sleeping bag": 700, "flip-flops": 300, "sweatpants": 500,
                  "sweatshirt": 550, "T-shirt": 300, "underwear": 400, "socks": 200, "woolen socks": 300,
                  "towel": 400, "raincoat": 400, "pot large": 600, "pot small": 400, "pot medium": 300,
                  "jornabor": 250, "corkscrew": 100, "salt": 100, "sugar": 700, "canned food": 2500,
                  "groats": 1800, "pasta": 2000, "condensed milk": 800, "tea": 200, "coffee": 300,
                  "matches": 100, "soap, comb, toothpaste, toothbrush": 300, "travel mat": 400, "tent": 3000,
                  "awning": 1000
                  }

print(f'Common weight of things: {sum(list_of_things.values())} g.')
for L in range(len(list_of_things) + 1):
    num = 0
    for subset in itertools.combinations(list(list_of_things.keys()), L):
        summ = 0
        for thing in subset:
            summ += list_of_things[thing]
        if summ <= MAX_WEIGHT:
            num += 1
            print(f'{num}. Вариант комплектации: {subset}. Общий вес: {summ}')
