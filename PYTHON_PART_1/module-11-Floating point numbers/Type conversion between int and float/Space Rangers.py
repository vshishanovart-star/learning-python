'Task 1. Space Rangers'

# In the distant (or maybe not so distant) future, you can buy a spaceship on some planet for half a loan (CR). One CR is 2200 chattles. Moreover, the chatles are indivisible and are always an integer. Write a simple currency converter program. The number of chat rooms is entered into the program, and it tells you how much CR it is and how many ships you can buy with this amount.

# Example 1:

# How many chats are there? 3150
# This is 1.4318181818181819 CR
# You can buy ships: 2

# Example 2:
# How many chats are there? 4400
# This is 2.0 CR
# You can buy ships: 4

# -------------------------------

'Задача 1. Космические рейнджеры'

# В далеком (а может и не очень) будущем на некоторой планете можно купить космический корабль за пол-кредита (CR). Один CR это 2200 чатлов. Причем чатлы неделимы и являются всегда целым числом. Напишите простую программу-конвертор валют. В программу вводится количество чатлов, а она сообщает сколько это CR и сколько кораблей можно купить на эту сумму.

# Пример 1:

# Сколько чатлов? 3150
# Это 1.4318181818181819 CR
# Можно купить кораблей: 2

# Пример 2:
# Сколько чатлов? 4400
# Это 2.0 CR
# Можно купить кораблей: 4

cr = 2200
chattles = int(input("Введите кол-во чатлов: "))
cost_spacecraft = cr / 2
purchaced_spacecraft = int(chattles / cost_spacecraft)
print("Колличество купленных космических кораблей:", purchaced_spacecraft)