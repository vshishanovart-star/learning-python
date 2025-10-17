('Задание 5. Наибольшая сумма цифр')

# Пользователь вводит N чисел.
# Среди натуральных чисел, которые он указал, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.

# Пример
# Введите количество чисел: 3
# Введите число: 5
# Введите число: 98
# Введите число: 453
# Число 98 имеет максимальную сумму цифр: 17


('Task 5. The largest sum of digits')

# The user enters N numbers.
# Among the natural numbers that he specified, find the largest by the sum of the digits.
# Display this number and the sum of its digits on the screen.

# Example
# Enter the number of numbers: 3
# Enter a number: 5
# Enter the number: 98
# Enter the number: 453
# The number 98 has a maximum sum of digits: 17


num_numbers = int(input("Введите количество чисел: "))
print()
sum = 0
name_number = ""

for num in range(num_numbers):
    while True:
        print("Введите натуральное число №", num + 1, ": ", end = "" )
        number = int(input())
        if number < 1:
            print("Ошибка! Число должно быть натуральным, то есть больше нуля. Попробуйте ещё раз")
        else:
            break
    sum_digits = 0
    for slider in str(number):
        sum_digits += int(slider)
    
    if sum_digits > sum:
        sum = sum_digits
        name_number = str(number)

        
print()
print("Число", name_number, "имеет максимальную сумму цифр:", sum)

    


    

        