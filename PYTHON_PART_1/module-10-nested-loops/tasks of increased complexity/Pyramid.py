"Task 1. Pyramid"

# # Write a program that receives the number of pyramid levels as input and displays them on the screen, filling them with odd numbers


"Задача 1. Пирамидка"

# # Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами


level_pyramid = int(input("Введите количество уровней пирамиды: "))
print()

num = 1

for row in range(1, level_pyramid + 1):
    print(" " * (level_pyramid - row), end="")   # пробелы перед числами
    for col in range(row):
        print(num, end=" ")
        num += 2
    print()                        # переход на новую строку










