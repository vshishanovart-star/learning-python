# ('Task 2. Stairs')

# Write a program that outputs a "ladder" of numbers when the user enters the number N.
# An empty print can be used to convert numbers to a new line.

# Example
# Enter a number: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5



# ('Задача 2. Лестница')

# Напишите программу, которая выводит «лестницу» из чисел, когда пользователь вводит число N.
# Для перевода чисел на новую строку допускается использование пустого print.

# Пример
# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

number_steps_ladder = int(input("Введите количество ступеней лестницы: "))
print()

for step in range(1, number_steps_ladder + 1):
  for step_length in range(step):
    print(step, end = "\t")
  print()