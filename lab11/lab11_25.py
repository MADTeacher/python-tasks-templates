from math import pow


# Напишите функцию algebraic_sum, на вход которой 
# подается два значения N и k (по умолчанию равно 2). 
# Функция должна возвращать результат следующего выражения: 1^k + 2^k + 3^k + … + N^k.
... # Ваш код


if __name__ == "__main__":
    N = int(input("Введите N "))
    k = int(input("Введите k "))

    print(algebraic_sum(N, k))
    print(algebraic_sum(N))
