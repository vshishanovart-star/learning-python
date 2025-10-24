'Task 1. Sports betting'

# We were hired by a bookmaker who conducts betting on equestrian sports. Write a program for calculating a player's potential winnings. To do this, enter his bet in rubles and the coefficient (a real number), and their product is displayed as a potential win.

# Example:

# How much are we betting? 1234
# What is the coefficient? 1.716
# Potential gain: 2117.544

# Complicating the task: make sure that no more than two digits are displayed after the dot.


'Задача 1. Ставки на спорт'

# Нас наняла букмекерская контора, где проводятся ставки на конный спорт. Напишите программу расчёта потенциального выигрыша игрока. Для этого вводится его ставка в рублях и коэффициент (вещественное число), а выводится их произведение в качестве потенциального выигрыша.

# Пример:

# Сколько ставим? 1234
# Какой коэффициент? 1.716
# Потенциальный выигрыш: 2117.544

# Усложнение задачи: сделайте так, чтобы после точки выводилось не больше двух цифр.

'Desision'

bet = int(input("Сколько ставим ? "))
cofficient = float(input("Какой коэффициент? "))
print()

winning = round(bet * cofficient, 2)
if winning - int(winning) == 0:
    winning = int(winning)
print("Ваш выигрыш составил:", winning)