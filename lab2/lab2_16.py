# Дан список. На его основе сформируйте новый, состоящий из первого, 
# среднего и последнего элемента первой переменной. 
# Полученный результат выведите в терминал.
from typing import Any


def app(my_list: list[Any]) -> None:
    ... # Ваш код


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, "a", "b", 2, 5]
    app(my_list)
