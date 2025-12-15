'Task 2. Comparison'

# Since operations with real numbers in Python can produce unexpected results (in particular, 0.1 + 0.2 will not exactly equal 0.3), the task is to deal with this somehow. 

# Write an eqv function that takes three numbers and then compares the sum of the first two numbers with the third one with a certain degree of accuracy: up to the 15th digit after the dot. If the equality holds, the function returns True, otherwise it returns False.

# Example 1:

# Enter the first number: 1.1
# Enter the second number: 2.2
# Enter the third number: 3.3

# True

# Example 2:

# Enter the first number: 1e-14
# Enter the second number: 1e-14
# Enter the third number: 3e-14
# False

# ---------------------------------

'Задача 2. Сравнение'

# Так как в Python операции с вещественными числами могут давать неожиданные результаты (в частности, 0.1 + 0.2 не будет в точности равняться 0.3), стоит задача с этим как-то справляться. 

# Напишите функцию eqv, которая принимает три числа и затем сравнивает сумму первых двух чисел с третьим с определённой степенью точности: до 15-го знака после точки. Если равенство выполняется, то функция возвращает True, иначе возвращает False.

# Пример 1:

# Введите первое число: 1.1
# Введите второе число: 2.2
# Введите третье число: 3.3
# True

# Пример 2:

# Введите первое число: 1e-14
# Введите второе число: 1e-14
# Введите третье число: 3e-14
# False

# ----------------------------------

def eqv(num_1, num_2, num_3):
    if round(num_1 + num_2, 15) == num_3:
        print(True)
    else:
        print(False)
        

number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
number_3 = float(input("Введите третье число: "))

eqv(number_1, number_2, number_3)