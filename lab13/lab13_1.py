# Напишите функцию create_counter, на вход которой подается 
# целочисленное значение, устанавливающее начальное состояние 
# счетчика. Функция должна возвращать другую функцию, 
# при вызове которой будет возвращаться обновленное значение 
# счетчика, увеличивающееся на единицу.

# Ваш код    


if __name__ == "__main__":
    val1 = 5
    x = create_counter(val1)
    print(x())
    print(x())

