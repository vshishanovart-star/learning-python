('Task 4. Prime numbers')

# Write a program that counts the number of primes in a given sequence and displays the answer on the screen.

# A prime number is divisible only by itself and by one.
# The sequence is set by calling input at each iteration of the loop. One iteration is one number.

# Example
# Enter the number of numbers: 6
# Enter a number: 4
# Enter the number: 7
# Enter a number: 20
# Enter the number: 3
# Enter a number: 11
# Enter the number: 37
# Number of prime numbers in the sequence: 4

# Recommendation:
# A prime number has only two divisors,
# therefore, to check, you need to iterate through all the numbers from one to it.
# If the hidden number is divisible without remainder by something other than one
# or yourself, then it's no longer a prime number.


('Задание 4. Простые числа')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу.
# Последовательность задаётся с помощью вызова ввода input на каждой итерации цикла. Одна итерация — одно число.

# Пример
# Введите количество чисел: 6
# Введите число: 4
# Введите число: 7
# Введите число: 20
# Введите число: 3
# Введите число: 11
# Введите число: 37
# Количество простых чисел в последовательности: 4

# Рекомендация:
# Простое число имеет только два делителя,
# поэтому для проверки нужно перебрать все числа от одного до него.
# Если загаданное число делится без остатка на что-то, кроме единицы
# или себя, то это уже не простое число.


num_numbers = int(input("Введите количество чисел: "))
prime_numbers_count = 0
print()

for num in range(num_numbers):
    number = int(input("Введите любое число, кроме нуля: "))
    for divider in range(1, number + 1):
        if number <= 1:
            print("Число непростое")
            break
        elif divider == number:
            print("Число простое")
            prime_numbers_count += 1
            break
        elif number % divider == 0 and divider != 1 and number != 2:
            print("Число непростое")
            break

print()
print("Количество простых чисел в последовательности:", prime_numbers_count)
