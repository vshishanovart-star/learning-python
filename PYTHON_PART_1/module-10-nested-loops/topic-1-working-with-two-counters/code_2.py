matrix = int(input("Введите размер матрицы: "))

for row in range(matrix):
    for col in range(matrix):
        if col == - row + matrix - 1:
            print("1", end = " ")
        elif col > - row + matrix - 1:
            print("2", end = " ")
        else:
            print("0", end = " ")
    print() 
