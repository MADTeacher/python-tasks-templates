# Напишите декоратор fahrenheit, который будет переводить в градусы Фаренгейта 
# возвращаемое значение функцией temperature_celsius, 
# на вход которой подается значение температуры в градусах Цельсия, 
# и оно же возвращается. 


# Код декоратора


@fahrenheit
# Код функции


if __name__ == "__main__":
    my_temp1 = 0
    print(temperature_celsius(my_temp1)) # 32
