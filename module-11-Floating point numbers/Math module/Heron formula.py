'Task 1. Heron'

# There is a so-called Heron formula that allows you to calculate the area of a triangle, knowing the lengths of its sides.

# S= √ (p * (p - a)*(p - b)*(p - c)) ,where

# S is the area;
# p is the half-perimeter of the triangle (a+b+c)/2;
# a,b,c are the lengths of the sides of the triangle.

# Write a program that takes the lengths of the sides of a triangle as input and outputs its area.

'Задача 1. Герон'

# Существует, так называемая, формула Герона, позволяющая вычислить площадь треугольника, зная длины его сторон.

# S= √ (p * (p - a)*(p - b)*(p - c)) ,где

# S - площадь;
# p - полупериметр треугольника (a+b+c)/2;
# a,b,c - длины сторон треугольника.

# Напишите программу, которая принимает на вход длины сторон треугольника и выводит его площадь

# ----------------------------------------------------------------------------------------------

a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))
import math
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Площадь треугольника равна:", s)