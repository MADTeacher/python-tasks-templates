# Напишите генераторную функцию list_mod, на вход которой 
# подается список целочисленных значений и значение k. 
# Функция должна возвращать только те элементы списка, 
# значение которых удовлетворяют следующему условию: list_mode[i] mod k == 0.

# Код генераторной функции


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 6, 4, 7, 8, 9]

    for i in list_mod(my_list, 5):
        print(i)
