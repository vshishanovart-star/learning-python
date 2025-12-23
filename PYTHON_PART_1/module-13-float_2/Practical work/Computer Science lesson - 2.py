'Task 1. Computer Science lesson — 2'

# Last time, the teacher wrote a program that outputs numbers in floating-point format, but he remembered that he had not taken into account one important thing: numbers can go from zero.
# What needs to be done

# A positive number x (x > 0) is set. Your task is to convert it to floating point format, that is

# , where 1 ≤ a < 10. Note that x is now greater than zero, not greater than one. Provide input control.

# Example 1

# Enter the number: 92345

# Floating point format: x = 9.2345 * 10 ** 4

# Example 2

# Enter a number: 0.0012

# Floating point format: x = 1.2 * 10 ** -3

# What is being evaluated

#     The output result matches the condition.
#     Input control is provided, the processed numbers are greater than zero.
#     The output format corresponds to the example.
#     The output contains a description of the result (the output numbers are accompanied by a text description).

# -------------------------------------------------------------------------------------------------------------------

'Задача 1. Урок информатики — 2'

# В прошлый раз учитель написал программу, которая выводит числа в формате плавающей точки, однако он вспомнил, что не учёл одну важную вещь: числа-то могут идти от нуля.
# Что нужно сделать

# Задано положительное число x (x > 0). Ваша задача — преобразовать его в формат плавающей точки, то есть a * 10 ** b ‌

# ‌, где 1 ≤ a < 10. Обратите внимание, что x теперь больше нуля, а не больше единицы. Обеспечьте контроль ввода.

# Пример 1

# Введите число: 92345

# Формат плавающей точки: x = 9.2345 * 10 ** 4

# Пример 2

# Введите число: 0.0012

# Формат плавающей точки: x = 1.2 * 10 ** -3

# Что оценивается

#     Результат вывода соответствует условию.
#     Обеспечен контроль ввода, обрабатываемые числа больше нуля.
#     Формат вывода соответствует примеру.
#     Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

# -----------------------------------------------------------------------------------------------

import math

while True:
    positive_number = float(input("Введите положительное число: "))
    if positive_number <= 0:
        print("Введённое число должно быть больше 0")
    else:
        break
      
degree = math.floor(math.log10(positive_number))
floating_point_number = positive_number / 10 ** degree

print("Формат плавающей точки:", positive_number, "=", floating_point_number, "* 10 **", degree)