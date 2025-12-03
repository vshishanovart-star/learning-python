'Task 2. The maximum of two'

# You have met an old friend who is also studying programming, but at a different educational institution. Over a cup of coffee, he complained that their erratic teacher had given them the task of writing a program that determines the largest of the two numbers entered, without using conditional operators, loops, and built-in functions like max/min/sorted. Glad that your course doesn't require this, you decide to help a friend anyway. Write a program for it.

# Example

# Enter the first number: 10

# Enter the second number: 5

# The largest number: 10

# Recommendations

#     Consider the difference of the sum and the difference of the numbers, the sum of the difference and the sum of the numbers.
#     If necessary, you can use the abs() function, which allows you to take the modulus of a number.

# When you are ready, proceed to the next material, which contains a video analysis of this task.

'Задача 2. Максимальное из двух'

# Вы встретились со старым другом, который тоже изучает программирование, но в другом учебном заведении. За чашкой кофе он пожаловался, что их сумасбродный преподаватель дал задание написать программу, которая из двух введённых чисел определяет наибольшее, не используя при этом условные операторы, циклы и встроенные функции вроде max/min/sorted. Радуясь, что на вашем курсе такого не требуют, вы всё-таки решаете помочь другу. Напишите для него программу.

# Пример

# Введите первое число: 10

# Введите второе число: 5

# Наибольшее число: 10

# Советы

#     Рассмотрите разность суммы и разности чисел, сумму разности и суммы чисел.
#     При необходимости можете использовать функцию abs(), позволяющую взять модуль числа.

# Когда будете готовы, переходите к следующему материалу, в котором представлен видеоразбор этого задания.

# ------------------------------------------------------------------------------------------------------

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
sum_numbers = first_number + second_number
difference_numbers = abs(first_number - second_number)
print(int((sum_numbers + difference_numbers) / 2))