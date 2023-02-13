import json

# Напишите функцию distance на вход которой подается 2 словаря 
# (point1 и point2) следующего вида: {''х'' : 10, ''у'' : 13} 
# (значение по умолчанию для point2). 
# Функция должна возвращать значение расстояния между заданными точками.
... # Ваш код


if __name__ == "__main__":
    point1: dict = json.loads(input("Введите словарь "))
    point2: dict = json.loads(input("Введите словарь "))
    print(distance(point1))
    print(distance(point1, point2))
