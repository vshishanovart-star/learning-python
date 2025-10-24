'Task 2. Birthday'

# In honor of his son's birthday, his father couldn't think of anything better than to give money. But he came up with a strange but interesting formula that calculates how much he will give: his son's age is multiplied by 1.5 and his body temperature. One can only envy such a fantasy.

# Write a program that asks the user for age (an integer) and body temperature (a real number) and outputs as a result how much money a father will give his son for his birthday.


'Задача 2. День рождения'

# В честь дня рождения сына отец не придумал ничего лучше, кроме как подарить денег. Зато он придумал хоть и странную, но интересную формулу, по которой высчитывается сколько он подарит: возраст сына умножается на 1.5 и на его температуру тела. Остаётся только позавидовать такой фантазии.

# Напишите программу, которая запрашивает у пользователя возраст (целое число) и температуру тела (вещественное число) и в результате выводит сколько отец подарит сыну денег на день рождения.


'Decision'

age = int(input("Введите возраст сына: "))
temperature = float(input("Введите температуру тела сына: "))
print()

gift_money = round(age * 1.5 * temperature, 2)
print('Сын получит на День Рождения', gift_money, "рублей.")


