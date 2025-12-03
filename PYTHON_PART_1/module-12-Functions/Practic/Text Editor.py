'Task 4. Text editor'

# We continue to develop a new text editor. Now we have been assigned to write a code for it that counts how many times any selected letter or number occurs in the text (and not just the letter "s", as was the case in task 3 of lesson "For Loop: iterating by line").
# What needs to be done

# Write a count_letters() function that accepts text as input and calculates the number of digits K and letters N. The function should display information about the letters and numbers found in a certain format.

# Example

# Enter the text: 100 years at lunch
# What number are we looking for? 0
# What letter are we looking for? l

# Number of digits 0: 2
# Number of letters L: 1

# -----------------------------------------

'Задача 4. Текстовый редактор'

# Продолжаем разрабатывать новый текстовый редактор. Теперь нам поручили написать для него код, который считает, сколько раз в тексте встречается любая выбранная буква или цифра (а не только буква «ы», как было в задаче 3 урока «Цикл for: итерирование по строке»).
# Что нужно сделать

# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и букв N. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

# Пример

# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л

# Количество цифр 0: 2
# Количество букв л: 1

# ----------------------------------------

def count_letters():
    text = input("Введите любой текст: ")
    desired_letter = input("Введите любую букву, колличество которых будем искать в тексте: ")
    desired_digit = int(input("Введите любую цифру, колличество которых будем искать в тесте: "))
    quantity_letters = 0
    quantity_digits = 0
    for letter in text:
        if letter == desired_letter:
            quantity_letters += 1
    print("Колличество букв '" + str(desired_letter) + "':", quantity_letters)
    for digit in text:
        if digit == str(desired_digit):
            quantity_digits += 1
    print("Колличество цифр '" + str(desired_digit) + "':", quantity_digits)

count_letters()
