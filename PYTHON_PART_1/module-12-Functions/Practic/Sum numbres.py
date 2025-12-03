"""Problem 1. The sum of the numbers
What needs to be done

Write a summa_n function that takes a single positive integer N and outputs the sum of all numbers from 1 to N inclusive.

An example of how the program works

Enter a number: 5

The sum of the numbers from 1 to 5 is 15

------------------------------------------

Задача 1. Сумма чисел
Что нужно сделать

Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N включительно.

Пример работы программы

Введите число: 5

Сумма чисел от 1 до 5 равна 15

------------------------------------------"""

def summa_n():
    n = int(input("Введите любое целое положительное число: "))
    summa_number = 0
    for num in range(1, n + 1):
        summa_number += num
    print("Сумма чисел от 1 до", n, "равна", summa_number)

summa_n()

# С использованием математической формулы

def summa_n():
    n = int(input("Введите любое целое положительное число: "))
    summa_number = int(n * (n + 1) / 2)
    print("Сумма чисел от 1 до", n, "равна", summa_number)

summa_n()
