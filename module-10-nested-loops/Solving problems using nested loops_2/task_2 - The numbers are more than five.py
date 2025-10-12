
# The user enters a sequence of N numbers. Write a program that counts the total number of digits greater than five in the entire sequence.

# Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее количество цифр больше пяти во всей последовательности.


sec_num = int(input("Введите колличество чисел в последовательности: "))
print()
count_num = 0
for num in range(1, sec_num + 1):
    print("Введите", num, "число: ", end = "")
    numeral = int(input())
    while numeral > 0:
        if (numeral % 10) > 5:
            count_num += 1
        numeral //= 10
print()
print("Кол-во цифр больше 5 во всех числах последовательности:", count_num)

