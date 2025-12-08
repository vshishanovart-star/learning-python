'Task 2. Testing'

# A team of programmers was given a new supercomputer model for testing. To begin with, the programmers decided to check how the computer is doing with the calculations of real numbers. The computer's developers warned that it only works with the exponential form of a number at the input.

# The user enters the number N in exponential form, where the mantissa is always a number from 1 to 9, and the order is less than zero. There is also a variable X, which is initially equal to one. Calculate how many times you need to add N to X to make it exceed two.

# Additionally: provide input control.

# Example 1:

# Enter the number in the exp. form: 1e-3
# Number of additions: 1001

'Задача 2. Тестирование'

# Команде программистов отдали на тестирование новую модель суперкомпьютера. Для начала программисты решили проверить, как у компьютера обстоят дела с вычислениями вещественных чисел. Разработчики компьютера предупредили, что на входе он работает только с экспоненциальной формой числа.

# Пользователь вводит число N в экспоненциальной форме, где мантисса всегда равна числу от 1 до 9, а порядок меньше нуля. Также есть переменная Х, которая изначально равна единице. Посчитайте, сколько раз нужно прибавить N к Х, чтобы оно перевалило за двойку.

# Дополнительно: обеспечьте контроль ввода.

# Пример 1:

# Введите число в эксп. форме: 1e-3
# Кол-во прибавлений: 1001

# Пример 2:

# Введите число в эксп. форме: 5.02e-1
# Кол-во прибавлений: 2

# Enter the number in the exp. form: 5.02e-1
# Number of additions: 2

# ------------------------------------------------

x = 1
count_operation = 0

n = float(input("Введите число в экспоненциальной форме от 1 до 9: "))
   
while x <= 2:
    x += n
    count_operation += 1
    print(x)

print("Колличество прибавлений:", count_operation)
