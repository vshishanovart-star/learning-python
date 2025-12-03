'The first digit'

# Given a positive number X, which consists of an integer and a fractional part. Print its first digit after the decimal point. When solving this problem, you cannot use a conditional construction, a loop, or strings.


'Первая цифра'

# Дано положительное число X, которое состоит из целой и дробной частей. Выведите его первую цифру после десятичной точки. При решении этой задачи нельзя пользоваться условной конструкцией, циклом или строками.

# ----------------------------------------------------------

x = float(input("Введите число с плавающей точкой: "))
first_number = x * 10 % 10
print("Первая цифра после десятичной точки:", int(first_number))