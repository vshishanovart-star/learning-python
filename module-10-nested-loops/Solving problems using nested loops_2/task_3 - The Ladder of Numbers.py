# The user enters the number N. Write a program that uses this number to generate a ladder of numbers like this:

# Пользователь вводит число N. Напишите программу, которая по этому числу выводит вот такую лестницу из чисел:

"""
Задача: Вывод числового треугольника

Пример выполнения:
┌───────────────────────────────┐
│ Введите число: 5              │
│                               │
│ 0 1 2 3 4 5                   │
│ 1 2 3 4 5                     │
│ 2 3 4 5                       │
│ 3 4 5                         │
│ 4 5                           │
│ 5                             │
└───────────────────────────────┘
"""

n = int(input("Введите любое число: "))
print()
for row in range(n + 1):
    for col in range(row, n + 1):
        print(col, end = " ")
    print()


