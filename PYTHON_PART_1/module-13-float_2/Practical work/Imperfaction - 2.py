'Task 4. Imperfection-2'

# You still work in the game development office and watch the programs of the former would-be programmer. In one of the games for children related to cartoon work with numbers, you had to write a code according to the following conditions: the program receives two numbers as input; the first number must have at least three digits, the second must have at least four, otherwise the program returns an error. If everything is fine, then in each number the first and last digits are swapped, and then their sum is displayed.

# And then you come across a program that was written by a previous programmer and that solves just such a problem. However, you have been asked to rewrite this code a bit so that it doesn't look so terrible. And it makes you feel uncomfortable, to put it mildly.

# Try to divide the logic of the code into three separate logical parts (functions):

#     count_numbers — gets a number and returns the number of digits in the number.;
#     change_number — gets a number, swaps the first and last digits in it, and returns the changed number.;
#     The main function receives nothing as input, requests the necessary data from the user inside, performs additional checks, and calls functions 1 and 2 to complete the task (checking and changing two numbers).

# What needs to be done

# Break down the program below into functions. There should be as few repetitions of the code as possible. Also, make sure that the main part of the program contains only the input of numbers, then the modified numbers and the output of their sum.

# first_n = int(input("Enter the first number: "))
# first_num_count = 0
# temp = first_n
# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10

# if first_num_count < 3:
# print("The first number has less than three digits.")
# else:
# last_digit = first_n % 10
#     first_digit = first_n // 10 ** (first_num_count - 1)
#     between_digits = first_n % 10 ** (first_num_count - 1) // 10
#     first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
#     print('The modified first number:', first_n)
#     second_n = int(input("\Enter the second number: "))
# second_num_count = 0
# temp = second_n

#     while temp > 0:
#         second_num_count += 1
#         temp = temp // 10
#     if second_num_count < 4:
#         print("The second number has less than four digits.")
# else:
# last_digit = second_n % 10
# first_digit = second_n // 10 ** (second_num_count - 1)
# between_digits = second_n % 10 ** (second_num_count - 1) // 10
# second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
#         print('The modified second number:', second_n)
# print('\The sum of the numbers:', first_n + second_n)

# What is being evaluated

#     The program is divided into several functions.
#     The conditions for the organization of the main body of the program are fulfilled.
     
# ----------------------------------------------------------------------------------------

'Задача 4. Недоделка-2'

# Вы всё так же работаете в конторе по разработке игр и смотрите программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако вас попросили немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится от него, мягко говоря, не по себе.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):

#     count_numbers — получает число и возвращает количество цифр в числе;
#     change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
#     main — функция ничего не получает на вход, внутри запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

# Что нужно сделать

# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

# first_n = int(input("Введите первое число: "))
# first_num_count = 0
# temp = first_n
# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10

# if first_num_count < 3:
#     print("В первом числе меньше трёх цифр.")
# else:
#     last_digit = first_n % 10
#     first_digit = first_n // 10 ** (first_num_count - 1)
#     between_digits = first_n % 10 ** (first_num_count - 1) // 10
#     first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
#     print('Изменённое первое число:', first_n)
#     second_n = int(input("\nВведите второе число: "))
#     second_num_count = 0
#     temp = second_n

#     while temp > 0:
#         second_num_count += 1
#         temp = temp // 10
#     if second_num_count < 4:
#         print("Во втором числе меньше четырёх цифр.")
#     else:
#         last_digit = second_n % 10
#         first_digit = second_n // 10 ** (second_num_count - 1)
#         between_digits = second_n % 10 ** (second_num_count - 1) // 10
#         second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
#         print('Изменённое второе число:', second_n)
#         print('\nСумма чисел:', first_n + second_n)

# Что оценивается

#     Программа разбита на несколько функций.
#     Выполнены условия по организации основного тела программы.

# --------------------------------------------------------------------------------------------------

def count_numbers(num):
    num_count = 0
    temp = num
    while temp > 0:
        num_count += 1
        temp //= 10
    return num_count
    

def change_numbers(num_1, num_2, digits_1, digits_2):
    last_digit_1, last_digit_2 = num_1 % 10, num_2 % 10
    first_digit_1, first_digit_2 = num_1 // 10 ** (digits_1 - 1), num_2 // 10 ** (digits_2 - 1)
    between_digits_1, between_digits_2 = num_1 % 10 ** (digits_1 - 1) // 10, num_2 % 10 ** (digits_2 - 1) // 10
    num_1, num_2 = last_digit_1 * 10 ** (digits_1 - 1) + between_digits_1 * 10 + first_digit_1, last_digit_2 * 10 ** (digits_2 - 1) + between_digits_2 * 10 + first_digit_2
    return num_1, num_2


def main():
    while True:
        first_n = int(input("Введите первое число, состоящее не менее, чем из 3 цифр: "))
        number_of_digits_1 = count_numbers(first_n)
        if number_of_digits_1 >= 3:
            break
        else:
            print("Число должно содержать в себе не менее трёх цифр!!! Попробуйте ещё раз")
    print()
    while True: 
        second_n = int(input("Введите второе число, состоящее не менее, чем из 4 цифр : "))
        number_of_digits_2 = count_numbers(second_n)
        if number_of_digits_2 >= 4:
            break
        else:
            print("Число должно содержать в себе не менее четырёх цифр!!! Попробуйте ещё раз")
    print()
    if number_of_digits_1 and number_of_digits_2:
        change_digits_1, change_digits_2 = change_numbers(first_n, second_n, number_of_digits_1, number_of_digits_2)
        print('Изменённое первое число:', change_digits_1)
        print('Изменённое второе число:', change_digits_2)
        print('Сумма чисел:', change_digits_1 + change_digits_2)


main()

