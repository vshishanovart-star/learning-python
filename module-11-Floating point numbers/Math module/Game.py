'Task 2. The game'

# You have to create a 2D game (top view, the player moves in two planes).

# Let's start with character control: we get from the player the distance traveled and the angle at which the character moved. Knowing this information, you need to change the current coordinates (0, 0) to new ones (x, y). To do this, you need to find out what distance the character will cover horizontally (on the X axis, x = distance × cosine of the angle) and vertically (on the Y axis, y = distance × sine of the angle).

# Write a program that gets the distance and angle of rotation as input. Print the coordinates of the character's new location.

'Задача 2. Игра'

# Вам предстоит создать 2D-игру (вид сверху, игрок двигается в двух плоскостях).

# Начнём с управления персонажем: получаем от игрока пройденное расстояние и угол, по которому двигался персонаж. Зная эту информацию, нужно изменить текущие координаты (0, 0) на новые (х, у). Чтобы это сделать, требуется узнать, какое расстояние персонаж преодолеет по горизонтали (по оси Х, x = расстояние × косинус угла) и по вертикали (по оси У, y = расстояние × синус угла).

# Напишите программу, которая получает на вход расстояние и угол поворота. Выведите координаты нового местоположения персонажа.

# -------------------------------------------------------------------------------------------------------------------------------

distance_traveled = float(input("Введите пройденное расстояние: "))
angle = float(input("Введите угол движения: "))
import math
angle = math.radians(angle)
horizontal_distance = round(distance_traveled * math.cos(angle), 2)
vertical_distance = round(distance_traveled * math.sin(angle), 2)
print("Координаты нового положения персонажа (" + str(horizontal_distance) + ",", str(vertical_distance) + ")")