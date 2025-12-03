'Task 1. Water'

# One bottle of Clearwater water from the VodZavod manufacturer costs differently in different stores.

# Write a program that calls the about_water function three times, passes one argument to it — the price of water, and displays the name of the water, the manufacturer, and the price.

'Задача 1. Вода'

# Одна бутылка воды «КлирВотер» от производителя «ВодЗавод» в разных магазинах стоит по-разному.

# Напишите программу, которая три раза вызывает функцию about_water, передаёт в неё один аргумент — цену на воду и выводит на экран название воды, производителя и цену.

# --------------------------------------------------

name_water = "КлирВотер"
manufacture = "ВодЗавод"


def about_water(price_water):
    print("Название:", name_water)
    print("Производитель:", manufacture)
    print("Цена:", price_water)
    print()

about_water(25)
about_water(30)
about_water(40)