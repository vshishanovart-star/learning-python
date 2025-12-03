"""Task 3. GPS Navigator 2.0

We were instructed to improve the GPS navigator by adding a new feature to it. Now the user can not only view the distance from himself to the object, but also set two arbitrary points in the navigator, after which the distance between them is displayed on the screen. To do this, the user enters four real numbers x1, y1, x2, y2 — these are just the coordinates of these two points.

Write a program where the user is asked what he wants — to find the distance from himself to a point or to find the distance between two arbitrary points, after which the necessary coordinates of the points are requested and the answer is displayed on the screen.

--------------------------------------

Задача 3. GPS-навигатор 2.0

Нам поручили усовершенствовать GPS-навигатор, добавив в него новую фишку. Теперь пользователь может не только смотреть расстояние от себя до объекта, но и задавать в навигаторе две произвольные точки, после чего на экран ему выводится расстояние между ними. Для этого пользователь вводит четыре действительных числа x1, y1, x2, y2 — это как раз координаты этих двух точек.

Напишите программу, где у пользователя спрашивается, чего он хочет — найти расстояние от себя до точки или найти расстояние между двумя произвольными точками, после чего запрашиваются необходимые координаты точек и выводится ответ на экран.

-------------------------------------"""
import math

def my_location(x, y):
    print('Расстояние до точки:' , math.sqrt(x ** 2 + y ** 2))

def between_points(x_1, y_1, x_2, y_2):
    print('Расстояние между точками:', math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2))
    
while True:   
    choice = int(input("Какое расстояние желаете измерить? От своего местоположения до точки на карте - '1', между точками на карте - '2': "))
    if choice == 1:
        x = float(input('Введите координату икс: '))
        y = float(input('Введите координату игрек: '))
        my_location(x, y)
    elif choice == 2:
        x_1 = float(input('Введите координату первой точки икс: '))
        y_1 = float(input('Введите координату первой точки игрек: '))
        x_2 = float(input('Введите координату второй точки икс: '))
        y_2 = float(input('Введите координату второй точки игрек: '))
        between_points(x_1, y_1, x_2, y_2)
    else:
        print('Вы ввели недопустимое значение')