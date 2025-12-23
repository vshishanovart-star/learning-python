'# Problem 2. The maximum function'

# Yura writes various useful functions for Python to make it easier for other programmers to work. He wanted to write a function that would find the maximum of the listed numbers. He already has a function for finding the maximum of two numbers. Yura wondered if it could be used to find the maximum of three numbers already.
# What needs to be done

# Help Yura write a program that finds a maximum of three numbers. To do this, use only the function of finding the maximum of two numbers.

# As a result, two functions should be implemented in the program:

#     maximum_of_two — the function takes two numbers and returns one (the largest of the two);
#     maximum_of_three — the function accepts three numbers and returns one (the largest of the three). In this case, it must use the first maximum_of_two function for comparisons.

# Example

# Enter the number: 5

# Enter a number: 1

# Enter a number: 23

# The largest number: 23
# What is being evaluated

#     The output result matches the condition.
#     The correct maximum of three numbers has been found.
#     The output contains a description of the result (the output numbers are accompanied by a text description).

# ---------------------------------------------------------------------------------------------------------------

'Задача 2. Функция максимума'

# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно использовать для нахождения максимума уже от трёх чисел?
# Что нужно сделать

# Помогите Юре написать программу, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:

#     maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
#     maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.

# Пример

# Введите число: 5

# Введите число: 1

# Введите число: 23

# Самое большое число: 23
# Что оценивается

#     Результат вывода соответствует условию.
#     Найден корректный максимум трёх чисел.
#     Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

# -----------------------------------------------------------------------------------------------

def maximum_of_two(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2


def maximum_of_three():
  
    number_1 = int(input("Введите любое число: "))
    number_2 = int(input("Введите любое число: "))
    number_3 = int(input("Введите любое число: "))
    
    max = maximum_of_two(number_1, number_2)
    max_all = 0
  
    if max > number_3:
        max_all = max
    else:
        max_all = number_3
      
    print("Максимальное из трёх чисел:", max_all)


maximum_of_three()