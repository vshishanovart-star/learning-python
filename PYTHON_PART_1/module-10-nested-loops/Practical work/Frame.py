('Task 3. Frame')

# Write a program that draws a rectangular frame using symbolic graphics.
# For vertical lines, use the vertical stroke symbol |,
# and for horizontal ones — hyphen - or underscore _.
# Let the width and height of the frame be determined by the user.

# Example
# |-----------------------------|
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |-----------------------------|


('Задача 3. Рамка')

# Напишите программу, которая рисует прямоугольную рамку с помощью символьной графики.
# Для вертикальных линий используйте символ вертикального штриха |,
# а для горизонтальных — дефис - или нижнее подчёркивание _.
# Пусть ширину и высоту рамки определяет пользователь.

# Пример
# |-----------------------------|
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |-----------------------------|

height = int(input("Введите высоту прямоугольной рамки: "))
width = int(input("Введите ширину прямоугольной рамки: "))
print()

for row in range(height):
  for col in range(width):
    if col == 0 or col == width - 1:
      print("|", end = "")
    elif row == 0 or row == height - 1:
      print("-", end = "")
    else:
      print(" ", end = "")
  print()