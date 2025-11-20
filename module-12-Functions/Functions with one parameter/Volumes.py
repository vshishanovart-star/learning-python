'Task 2. These are the volumes of 2'

# Andrey continues to write his physics term paper, and now he needs to find not only the volume of the planet, but also its area. To do this, he uses two such formulas:


# The formula for the area of a sphere:


#             S = 4 ⋅ π ⋅ R 2


# The formula for the volume of the ball:


#             V = 4/3 * π * r³


# Since these formulas will be useful more than once in the course project itself, Andrey decided to act rationally and simply write a function for each formula.

# Write a program that receives the radius of the planet (a real number) from the user as input and calls the functions sphere_area and sphereVolume. Implement these functions: the first calculates and displays the area of the sphere, the second — the volume of the ball.

'Задача 2. Вот это объёмы 2'

# Андрей продолжает писать курсовую работу по физике, и теперь ему нужно находить не только объём планеты, но и её площадь. Для этого он использует две такие формулы:


# Формула для площади сферы:

# ‌
#           S = 4 ⋅ π ⋅ R 2
# ‌


# Формула для объёма шара:

# ‌
#           V = 4/3 * π * r³
# ‌

# Так как в самом курсовом проекте эти формулы пригодятся ещё не раз, Андрей решил поступить рационально и просто написать функцию для каждой формулы.

# Напишите программу, которая на вход получает от пользователя радиус планеты (вещественное число) и вызывает функции sphere_area и sphereVolume. Реализуйте эти функции: первая считает и выводит на экран площадь сферы, вторая — объём шара.

# --------------------------------------------------------------------------------------------------
import math
def sphere_area(radius):
        print("Площадь поверхности планеты:", 4 * math.pi * radius ** 2)
def sphere_volume(radius):
        print("Объём шара:", 4 / 3 * math.pi * radius ** 3)
while True:
    radius = float(input("Введите радиус планеты: "))
    print()

    sphere_area(radius)
    sphere_volume(radius)
    print()