'Task 3. Prime numbers'

# The user enters the number N, which is the number of numbers in the sequence. Write the is_prime function, which checks if the number is prime and outputs the answer to the console.

'Задача 3. Простые числа'

# Пользователь вводит число N — количество чисел в последовательности. Напишите функцию  is_prime, которая проверяет, является ли число простым и выводит ответ в консоль.

# ---------------------------------

n = int(input("Введите количество чисел: "))
print()

def is_prime(n):
    count_prime_number = 0
    # Проверяем все числа от 0 до n
    for current_num in range(n + 1):
        if current_num < 2:
            continue  # пропускаем 0 и 1
        
        is_prime = True
        # Проверяем, простое ли current_num
        for divisor in range(2, int(current_num**0.5) + 1):
            if current_num % divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            print("Простое число:", current_num)
            count_prime_number += 1
    
    print("Количество простых чисел в последовательности:", count_prime_number)

is_prime(n)
