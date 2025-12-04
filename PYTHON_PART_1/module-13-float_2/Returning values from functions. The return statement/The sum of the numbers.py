'Problem 1. The sum of the numbers 2'

# The user enters the number N. Write a summa_n function that takes a single positive integer N and finds the sum of all numbers from 1 to N inclusive. The function is called two times: first from the number N, and then from the amount received.

# -------------------------------------------------------------------------

'Задача 1. Сумма чисел 2'

# Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N и находит сумму всех чисел от 1 до N включительно. Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.

# -------------------------------------------------------------------------

def sum_numbers(num):
    sum_count = 0
    for i in range(1, num + 1):
        sum_count += i
    return sum_count


n = int(input("Введите целое положительное число: "))

x = sum_numbers(n)

x_2 = sum_numbers(x)

print(x)
print(x_2)
