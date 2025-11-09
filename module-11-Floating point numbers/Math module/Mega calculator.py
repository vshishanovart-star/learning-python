'Task 3. Mega Calculator'

# Kesha is in the third grade, and already knows how to program in python. Like many of his classmates, he really likes to put all the knowledge he has gained into practice at once. Yesterday, Kesha found out about the math module and its main features, so he decided to write a mega calculator that would apply all functions at once to the number entered by the user. In order not to forget anything, he uses a cheat sheet that was attached to the lesson.

# Write a program that receives a real number from the user, applies the functions of the Math module to it in turn, and outputs the result.:

#     rounds down
#     rounds up
#     takes the modulus of a number
#     extracts the square root
#     raises the exponent to a power equal to the number
#     counts the natural logarithm of a number
#     counts the logarithm of a number based on 2
#     counts the logarithm of a number based on 10
#     counts the sine and cosine of a number

# And since Kesha is the smartest in the class, he decided to try to calculate the factorial of the number. To do this, he had to come up with and implement input control: the factorial is calculated only if the entered number was natural.

'Задача 3. Мега-калькулятор'

# Кеша учится в третьем классе, и уже умеет программировать на питоне. Как и многие его одноклассники, он очень любит сразу применять все полученные знания на практике. Вчера Кеша узнал про модуль math и его основные возможности, поэтому решил написать мега-калькулятор, который бы применял сразу все функции к введенному пользователем числу. Чтобы ничего не забыть, он пользуется шпаргалкой, которую прикрепили к уроку

# Напишите программу, которая получает от пользователя вещественное число, по очереди применяет к нему функции модуля Math и выводит результат:

#     округляет вниз
#     округляет вверх
#     берет модуль числа
#     извлекает квадратный корень
#     возводит экспоненту в степень, равную числу
#     считает натуральный логарифм числа
#     считает логарифм числа по основанию 2
#     считает логарифм числа по основанию 10
#     считает синус и косинус числа

# И так как Кеша самый умный в классе, он решил попробовать посчитать факториал числа. Для этого ему пришлось придумать и реализовать контроль ввода: факториал вычисляется, только если введенное число было натуральным.

# ------------------------------------------------------------

real_number = float(input("Введите вещественное число: "))
import math
math_function = [math.floor, math.ceil, abs, math.sqrt, math.exp, math.log, math.log2, math.log10, math.sin, math.cos, math.factorial]
for function in math_function:
    if function == math.factorial:
        if real_number == int(real_number) and real_number >= 0:
            print(function(int(real_number)))
    else:
        print(function(real_number))

