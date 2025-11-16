'Task 1. Knights move'

# As part of the development of chess AI, there is a new task: using the given real coordinates of the knight and the point, the program must determine whether the knight can walk to this point. Use as few if constructs and logical operators as possible. Provide input control.

# An example of how the program works

# Enter the horse's location:

# 0.071

# 0.118

# Enter the location of the point on the board:

# 0.213

# 0.068

# The knight in the cage is (0, 1). The dot in the cage is (2, 0).

# Yes, the horse can walk to this point.

# When you are ready, click the button below to see the solution to the problem.

'Задача 1. Ход конём'

# В рамках разработки шахматного ИИ стоит новая задача: по заданным вещественным координатам коня и точки программа должна определить, может ли конь ходить в эту точку. Используйте как можно меньше конструкций if и логических операторов. Обеспечьте контроль ввода.

# Пример работы программы

# Введите местоположение коня:

# 0.071

# 0.118

# Введите местоположение точки на доске:

# 0.213

# 0.068

# Конь в клетке (0, 1). Точка в клетке (2, 0).

# Да, конь может ходить в эту точку.

# Когда будете готовы, нажмите кнопку ниже, чтобы посмотреть решение задачи.

# ---------------------------------------------------------------------------

horse_x = float(input("Введите местоположение коня по горизонтали: "))
horse_y = float(input("Введите местоположение коня по вертикали: "))
dot_board_x = float(input("Введите координаты точки по горизонтали: "))
dot_board_y = float(input("Введите кординаты точки по вертикали: "))
knights_cage_x = int(horse_x * 10)
knights_cage_y = int(horse_y * 10)
cage_x = int(dot_board_x * 10)
cage_y = int(dot_board_y * 10)
delta_x = abs(knights_cage_x - cage_x)
delta_y = abs(knights_cage_y - cage_y)

if not (0 <= knights_cage_x <= 7 and 0 <= knights_cage_y <= 7 and 0 <= cage_x <= 7 and 0 <= cage_y <= 7):
    print("Заданы координаты, выходящие за границы шахматной доски")
    exit()

print("Конь в клетке:", "(" + str(knights_cage_x) + ",", str(knights_cage_y) + ")")
print("Точка в клетке:", "(" + str(cage_x) + ",", str(cage_y) + ")")

if delta_x == 1 and delta_y == 2 or delta_x == 2 and delta_y == 1:
    print("Да, конь может ходить в эту точку")
else:
    print("Нет, конь не может пойти в эту клетку")