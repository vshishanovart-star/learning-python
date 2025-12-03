'These are the volumes!'

# For his physics term paper, Andrey needs to compare the volumes of two planets: Earth and a planet theoretically possible for our universe. Andrey is good at formulas, but he doesn't count well. The volume of the Earth is known to him in advance - this is 10.8321 * 10 ** 11 km3

# He needs to calculate the volume of a theoretically possible planet. He has a formula:

# V = 4/3∙π∙R³

# In it, V is the volume, π is the number pi, and R is the radius of the planet.

# What needs to be done

# Write a program that receives the radius of a random planet as input and displays on the screen how many times the planet Earth is smaller or larger than a theoretically possible planet in volume. Round the answer to three digits after the dot.

# Example 1

# radius = 3389.5

# At the exit:

# The volume of the planet Earth is 6.641 times larger

# Example 2

# radius = 7000

# At the exit:

# The volume of the planet Earth is 1.326 times smaller

# What is being evaluated

#     The output result matches the condition, and the output format matches the example.

#     The output contains a description of the result (the output numbers are accompanied by a text description).


'Вот это объёмы!'

# Для курсовой работы по физике Андрею нужно сравнить объёмы двух планет: Земли и теоретически возможной для нашей Вселенной планеты. Андрей хорошо разбирается в формулах, но плохо считает. Объём Земли ему известен заранее - это 10.8321 * 10 ** 11 км3

# Объём теоретически возможной планеты ему нужно посчитать. У него есть формула:‌

# V = 4/3∙π∙R³

# ‌В ней V — это объём, π — число пи, а R — радиус планеты.

# Что нужно сделать

# Напишите программу, которая получает на вход радиус случайной планеты и выводит на экран, во сколько раз планета Земля меньше или больше теоретически возможной планеты по объёму. Ответ округлите до трёх знаков после точки.

# Пример 1

# radius = 3389.5

# На выходе:

# Объём планеты Земля больше в 6.641 раз

# Пример 2

# radius = 7000

# На выходе:

# Объём планеты Земля меньше в 1.326 раз

# Что оценивается

#     Результат вывода соответствует условию, а формат вывода соответствует примеру.

#     Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

#     ------------------------------------------------------------------------------------

import math

radius_exoplanet = float(input("Введите радиус экзопланеты: "))
volume_earth = 10.8321 * math.pow(10, 11)

volume_exoplanet = 4/3 * math.pi * math.pow(radius_exoplanet, 3)

if volume_earth > volume_exoplanet:
    print("Объём планеты Земля больше в", round(volume_earth / volume_exoplanet, 3), "раз")
else:
    print("Объём планеты Земля меньше в", round(volume_exoplanet / volume_earth, 3), "раз")