'Task 2. Computer vision'

# You are participating in the development of a robot that plays chess on a real, physical 0.8 x 0.8 meter chessboard. The robot looks at the board with the camera and sees the location of the pieces in real numbers with very high accuracy.

# Write a program that enters the real coordinates of a chess piece, and the program determines which square of the board this piece is located in. Each square of the board has a size of 10x10 cm and integer coordinates consisting of two numbers. For example, the upper left cell has integer coordinates (0, 0), the cell to its right is (1, 0) and the cell below is (0, 1). Also, ensure input control: you cannot go beyond the boundaries of the board.

# Example:

# Enter the shape's location
# Horizontal: 0.731
# Vertical: 0.149

# The figure is in the cell (7, 1)

# Enter the shape's location
# Horizontal: 0.833
# Vertically: -0.132

# There is no cell with such a coordinate.

# ---------------------------------------

'Задача 2. Компьютерное зрение'

# Вы участвуете в разработке робота, который играет в шахматы на реальной, физической шахматной доске размером 0.8 х 0.8 метра. Робот смотрит камерой на доску и видит расположение фигур в вещественных числах с очень высокой точностью.

# Напишите программу, в которую вводятся вещественные координаты шахматной фигуры, а программа определяет в какой клетке доски находится эта фигура. Каждая клетка доски имеет размер 10х10 см и целочисленные координаты, состоящие из двух чисел. Например левая верхняя клетка имеет целые координаты (0, 0), справа от неё клетка (1, 0) а снизу (0, 1). Также обеспечьте контроль ввода: нельзя выходить за границы доски.

# Пример:

# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.149

# Фигура находится в клетке (7, 1)

# Введите местоположение фигуры
# По горизонтали: 0.833
# По вертикали: -0.132

# Клетки с такой координатой не существует


while True:
    x = float(input("Введите местоположение фигуры по горизонтали: "))
    y = float(input("Введите местоположение фигуры по вертикали: "))
    if x < 0 or x > 0.8 or y < 0 or y > 0.8:
        print("Данные координаты местоположения не допустими!!!")
        continue
    x_square = int(10 * x)
    y_square = int(10 * y)
    print("Местоположение шахматной фигуры: ", x_square, ",", y_square, sep = "")

