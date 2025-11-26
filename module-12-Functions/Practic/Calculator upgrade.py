'Task 3. Upgrade the calculator'

# Stepan uses a calculator to calculate the sum and difference of numbers, but at work he requires more than just the usual arithmetic operations. He doesn't want to do anything manually, so he decided to expand the calculator's functionality a bit.
# What needs to be done

# Write a program that asks the user for a number and the action to do with the number: output the sum of its digits, the maximum or minimum digit. Design each action as a separate function, and loop the main program.

# The requested numbers must be passed to the sum, maximum, and minimum functions using arguments.

# Example 1
	

# Example 2
	

# Example 3

# Enter the number: 984

# Enter the action number:
# 1 - the sum of the digits
# 2 is the maximum number
# 3 is the minimum number: 1

# Total of digits: 21
	

# Enter the number: 546

# Enter the action number:
# 1 - the sum of the digits
# 2 is the maximum number
# 3 - minimum number: 2

# Maximum number: 6
	

# Enter a number: 741

# Enter the action number:
# 1 - the sum of the digits
# 2 is the maximum number
# 3 - minimum number: 3

# Minimum number: 1

# ---------------------------------

'Задача 3. Апгрейд калькулятора'

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. Он ничего не хочет делать вручную, поэтому решил немного расширить функциональность калькулятора.
# Что нужно сделать

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

# Пример 1
	

# Пример 2
	

# Пример 3

# Введите число: 984

# Введите номер действия:
# 1 - сумма цифр
# 2 - максимальная цифра
# 3 - минимальная цифра: 1

# Сумма цифр: 21
	

# Введите число: 546

# Введите номер действия:
# 1 - сумма цифр
# 2 - максимальная цифра
# 3 - минимальная цифра: 2

# Максимальная цифра: 6
	

# Введите число: 741

# Введите номер действия:
# 1 - сумма цифр
# 2 - максимальная цифра
# 3 - минимальная цифра: 3

# Минимальная цифра: 1

# ------------------------------

def sum_digits(num):
    num = str(num)
    count_num = 0
    for summa in num:
        count_num += int(summa)
    print("Сумма цифр:", count_num)

def max_digit(num):
    num = str(num)
    max_num = 0
    for maximum in num:
        if int(maximum) > max_num:
            max_num = int(maximum)
    print("Максимальная цифра:", max_num)

def min_digit(num):
    num = str(num)
    min_num = int(num[0])
    for minimum in num:
        if int(minimum) < min_num:
            min_num = int(minimum)
    print("Минимальная цифра:", min_num)

while True:
    print("Введите число")
    number = int(input())
    print("Введите номер действия:\n"
          "1 - сумма цифр\n"
          "2 - максимальная цифра\n"
          "3 - минимальная цифра")
    action_number = int(input())
    if action_number == 1:
        sum_digits(number)
    elif action_number == 2:
        max_digit(number)
    elif action_number == 3:
        min_digit(number)

# Математический способ без преобразования чисел в строки

def sum_digits(num):
  count_num = 0
  while num > 0:
      last_digit = num % 10
      count_num += last_digit
      num = num // 10 
  print("Сумма цифр:", count_num )

def max_digit(num):
  max_num = 0
  while num > 0:
      last_digit = num % 10
      if last_digit > max_num:
          max_num = last_digit
      num = num // 10
  print("Максимальная цифра:", max_num)

def min_digit(num):
  temp_num = num
  while temp_num >= 10:
      temp_num = temp_num // 10
  min_num = temp_num
  while num > 0:
      last_digit = num % 10
      if last_digit < min_num:
          min_num = last_digit
      num = num // 10
  print("Минимальная цифра:", min_num)

while True:
  print("Введите число")
  number = int(input())
  print("Введите номер действия:\n"
        "1 - сумма цифр\n"
        "2 - максимальная цифра\n"
        "3 - минимальная цифра")
  action_number = int(input())
  if action_number == 1:
      sum_digits(number)
  elif action_number == 2:
      max_digit(number)
  elif action_number == 3:
      min_digit(number)




