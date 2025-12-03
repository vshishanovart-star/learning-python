'The Greatest Common Divisor problem'

# The greatest common divisor (GCD) is the largest number by which two or more numbers can be divided without remainder.

# For example, the largest common divisor for the numbers 12 and 15 will be the number 3, because 3 is the largest number by which 12 and 15 can be divided without remainder. 
# What needs to be done

# Write a function that calculates the greatest common divisor of two numbers.

# An example of how the program works:

# Enter the first number: 30
# Enter the second number: 18
# Largest common divisor: 6

# Click the button below to get a hint on how to solve the problem.

# ------------------------------------------------------------------


'Задача «Наибольший общий делитель»'

# Наибольший общий делитель (НОД) — это самое большое число, на которое можно разделить два или более числа без остатка.

# Например, наибольшим общим делителем для чисел 12 и 15 будет число 3, потому что 3 — это самое большое число, на которое можно без остатка разделить 12 и 15. 
# Что нужно сделать

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел.

# Пример работы программы:

# Введите первое число: 30
# Введите второе число: 18
# Наибольший общий делитель: 6

# Нажмите кнопку ниже, чтобы получить подсказку по решению задачи.

# -----------------------------------------------------------------

def greatest_number_divisor(number_1, number_2):
    greatest_divisor = 0
    smallest_number = min(number_1, number_2)
    hypothetical_divisor = smallest_number
    while hypothetical_divisor > 0: 
        if number_1 % hypothetical_divisor == 0 and number_2 % hypothetical_divisor == 0:
            break
        hypothetical_divisor -= 1
    greatest_divisor = hypothetical_divisor
    print("Наибольший общий делитель:", greatest_divisor)


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))


greatest_number_divisor(first_number, second_number)

