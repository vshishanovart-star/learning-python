'Task 3. Precision and accuracy'

# The robot from the Computer Vision task correctly determines which square the pieces are on. But the trouble is, often due to the fault of a human opponent, the pieces on the board are not exactly in the center of the cell, but with an offset. If this displacement becomes too large during the game, it will become unclear which square the piece was in. To avoid this situation, you need the robot to adjust the pieces on the board, placing them in the center of the cell. Modify the Computer Vision program so that it gives out not only the numbers of the cell in which the figure is located, but also two real corrections: how much you need to move the figure horizontally and vertically so that it is in the center of its cell.

# Example:

# Enter the shape's location
# Horizontal: 0.731
# Vertical: 0.167
# The figure is in the cell (7, 1)
# Adjust the position of the figure to (0.019, -0.017)

# -----------------------------------------------------

'Задача 3. Точность и аккуратность'

# Робот из задачи “Компьютерное зрение” правильно определяет на какой клетке стоят фигуры. Но вот беда, часто по вине соперника-человека фигуры стоят на доске не ровно по центру клетки, а со смещением. Если во время игры такое смещение станет слишком велико, то станет непонятно в какой клетке стояла фигура. Чтобы избежать этой ситуации нужно чтобы робот поправлял фигуры на доске, выставляя их по центру клетки. Модифицируйте программу “Компьютерное зрение” так, чтобы она выдавала не только номера клетки, в которой находится фигура но и две вещественных поправки: на сколько нужно подвинуть фигуру по горизонтали и вертикали для того чтобы она оказалась по центру своей клетки.

# Пример:

# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.167
# Фигура находится в клетке (7, 1)
# Поправьте положение фигуры на (0.019, -0.017)


# ---------------------------------------------


while True:
    x = float(input("Введите местоположение фигуры по горизонтали: "))
    y = float(input("Введите местоположение фигуры по вертикали: "))
    if x < 0 or x > 0.8 or y < 0 or y > 0.8:
        print("Данные координаты местоположения не допустими!!!")
        continue
    x_square = int(10 * x)
    y_square = int(10 * y)
    print("Местоположение шахматной фигуры: (", x_square, ",", y_square, ")")
    ideal_position_center_x = (x_square + 0.5) * 0.1
    ideal_position_center_y = (y_square + 0.5) * 0.1
    if x > ideal_position_center_x:
        horizontal_offset = round(x - ideal_position_center_x, 3)
        print("Сместить по горизонтали на -", horizontal_offset, "метра")
    elif x < ideal_position_center_x:
        horizontal_offset = round(ideal_position_center_x - x, 3)
        print("Сместить по горизонтали на", horizontal_offset, "метра")
    else:
        print("Положение фигуры идеально по центру")
    if y > ideal_position_center_y:
        vertical_offset = round(y - ideal_position_center_y, 3)
        print("Сместить по горизонтали на -", vertical_offset, "метра")
    elif y < ideal_position_center_y:
        vertical_offset = round(ideal_position_center_y - y, 3)
        print("Сместить по вертикали на", vertical_offset, "метра")
    else:
        print("Положение фигуры идеально по центру")

    

