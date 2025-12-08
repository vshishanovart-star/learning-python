'Task 3. Computer science lesson'

# In one of the computer science lessons, the teacher explained the topic "Floating point numbers", but several students could not understand why this point "floats" and what numbers look like in this form. For clarity, the teacher wrote a program that takes a number greater than ten and outputs it in floating-point format.

# The user enters a positive number x (x > 10). Write a function that outputs it in floating point format, that is, x = a *10 ** b, where 1 ≤ a < 10.

# Example 1:

# Enter a number: 16
# Floating point format: x = 1.6 * 10 ** 1

# Example 2:

# Enter the number: 92345
# Floating point format: x = 9.2345 * 10 ** 4

# ----------------------------------------------

'Задача 3. Урок информатики'

# На одном из уроков информатики учитель объяснял тему «Числа с плавающей точкой», но несколько учеников никак не могли понять, почему эта точка «плавает» и как вообще выглядят числа в такой форме. Для наглядности учитель написал программу, которая берёт число больше десяти и выводит его в формате плавающей точки.

# Пользователь вводит положительное число x (x > 10). Напишите функцию, которая выводит его в формате плавающей точки, то есть x = a *10 ** b, где 1 ≤ a < 10.

# Пример 1:

# Введите число: 16
# Формат плавающей точки: x = 1.6 * 10 ** 1

# Пример 2:

# Введите число: 92345
# Формат плавающей точки: x = 9.2345 * 10 ** 4

# -----------------------------------------------

n = float(input("Введите любое число больше 10: "))
degree_idicator = 0
while n >= 10:
    n /= 10
    degree_idicator += 1
print("Число в формате плавающей точки:", n, "* 10 **", degree_idicator)