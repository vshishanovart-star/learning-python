'Problem 3. The number is reversed'

# What needs to be done

# The user enters two numbers: N and K.

# Write a program that turns over each of the entered numbers, that is, writes these numbers in reverse order.

# Example

# Enter the first number: 102
# Enter the second number: 123

# The first number is reversed: 201
# The second number is the opposite: 321
# What is being evaluated

#     The problem is solved using a function that flips a number.
#     The output result matches the condition, and the output format matches the example.
#     The output contains a description of the result (the output numbers are accompanied by a text description).

# ----------------------------------------------------------------------------------------------------------------

'Задача 3. Число наоборот'

# Что нужно сделать

# Пользователь вводит два числа: N и K.

# Напишите программу, которая переворачивает каждое из введённых чисел, то есть записывает эти числа в обратном порядке.

# Пример

# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321
# Что оценивается

#     Задача решена с использованием функции, которая переворачивает число.
#     Результат вывода соответствует условию, а формат вывода соответствует примеру.
#     Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

# ----------------------------------------------------------------------------------------------

def number_reversed(num_1, num_2):
    revers, revers_2 = "", ""
  
    while num_1 != 0 or num_2 != 0:
      if num_1 != 0:
          last_digit = num_1 % 10
          num_1 //= 10
          revers += str(last_digit)
      if num_2 != 0:
          last_digit_2 = num_2 % 10
          num_2 //= 10
          revers_2 += str(last_digit_2)
      
    print("Первое число наоборот:", revers)
    print("Второе число наоборот:", revers_2)


number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

number_reversed(number_1, number_2)
