# Напишите декоратор upcase_result, который будет переводить 
# все символы результирующего значения функции reverse_str 
# в верхний регистр. На вход функции reverse_str подается 
# строка и возвращается ее инвертированное представление.


# Код декоратора


@upcase_result
# Код функции


if __name__ == "__main__":
    my_str1 = "qwerty"
    print(reverse_str(my_str1)) # YTREWQ
