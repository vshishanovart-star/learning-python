'Task 1. Taxes again'

# The government of one of the countries has an accounting program that summarizes the taxes of its citizens and companies plus VAT on goods. The country was developing, total taxes were increasing, and accountants noticed that after adding some VAT from a product to the total amount of taxes, the total amount stopped changing… 

# We need to help the accountants: write a function that inputs two numbers — the total amount of tax and the new tax new_tax, which must be added to the total amount. The function should check whether the exponent of e changes when adding two numbers.

# Example 1:

# Enter the country's budget: 1.2e-12
# New income (tax): 1.2e1
# The result: The budget will increase

# Example 2:

# Enter the country's budget: 1.23e12
# New income (tax): 1.2e1
# Result: The budget will not change.

# ---------------------------------------

'Задача 1. Опять налоги'

# У правительства одной из стран есть бухгалтерская программа, которая суммирует налоги её граждан, компаний плюс НДС с товаров. Страна развивалась, суммарные налоги увеличивались, и бухгалтеры заметили, что после добавления к общей сумме налогов некого НДС от какого-то продукта общая сумма перестала меняться… 

# Нужно помочь бухгалтерам: напишите функцию, на вход которой подаются два числа — общая сумма налога tax и новый налог new_tax, который нужно добавить к общей сумме. Функция должна проверять, изменится ли показатель степени e при сложении двух чисел.

# Пример 1:

# Введите бюджет страны: 1.2e-12
# Новые поступления (налог): 1.2e1
# Результат: Бюджет увеличится

# Пример 2:

# Введите бюджет страны: 1.23e12
# Новые поступления (налог): 1.2e1
# Результат: Бюджет не изменится

# --------------------------------------

def sum_tax(taxes, vallue_added_tax):
    total_tax = taxes + vallue_added_tax
    print("Величина общих налоговых сборов составит:", total_tax, end=" ")
    if total_tax > taxes:
        print("Бюджет увеличится")
    else:
        print("Бюджет не изменится")


tax = float(input("Введите общую сумму налога: "))
new_tax = float(input("Введите размер нового налога: "))

sum_tax(tax, new_tax)

