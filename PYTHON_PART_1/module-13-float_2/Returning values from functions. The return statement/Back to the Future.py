'Task 2. "Back to the future"'

# You are one of the developers of the Python programming language, and you are writing a special mathematical module that could simply be plugged into the program and make life easier for all programmers.

# Implement the gcd function, which gets two parameters — two numbers — and returns the largest common divisor of these two numbers.

# -------------------------------------------

'Задача 2. «Назад в будущее»'

# Вы — один из разработчиков языка программирования Python, и вы пишете специальный математический модуль, который можно было бы просто подключить внутри программы и облегчить жизнь всем программистам.

# Реализуйте функцию gcd, которая получает два параметра — два числа — и возвращает наибольший общий делитель этих двух чисел.

# ------------------------------------------
import math


def gcd(num, num_2):
    greatest_common_divisor = math.gcd(num, num_2)
    return greatest_common_divisor


number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

gcd(number_1, number_2)

print("Наибольший общий делитель:", gcd(number_1, number_2))




