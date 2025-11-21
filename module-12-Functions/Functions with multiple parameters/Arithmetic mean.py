'Problem 1. Arithmetic mean'

"""The program receives two numbers from the user — a and b. Implement a function that accepts the numbers a and b as input, counts and outputs to the console the arithmetic mean of all the numbers from the segment [a; b]. Ensure input control: do not forget that a should always be less than b.

Example:

Enter the left border: 3

Enter the right border: 8

Average: 5.5


Complication: do this without using loops.

---------------------------------------------------------"""

'Задача 1. Среднее арифметическое'

"""Программа получает от пользователя два числа — a и b. Реализуйте функцию, которая принимает на вход числа a и b, считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b]. Обеспечьте контроль ввода: не забывайте, что а всегда должно быть меньше, чем b.

Пример:

Введите левую границу: 3

Введите правую границу: 8

Среднее: 5.5


Усложнение: сделайте это без использования циклов.

---------------------------------------------------------"""
def arithmetic_mean(a, b):
    if a >= b:
        print("Число 'a' должно быть меньше числа 'b' !")
    sum = 0
    quantity_num = 0
    for num in range(a, b + 1):
        sum += num
        quantity_num += 1
    print("Среднее арифметическое всех чисел из отрезка:", sum / quantity_num)


a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))
arithmetic_mean(a, b)

"""-----------------------------------------------------------"""

def arithmetic_mean(a, b):
    if a >= b:
        print("Число 'a' должно быть меньше числа 'b' !")
    sum_num = (a + b) / 2
    print("Среднее арифметическое всех чисел из отрезка:", sum_num)

a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))
arithmetic_mean(a, b)
    
