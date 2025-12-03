('Task 6. A triangle of hashtags')

# Write a program that displays an isosceles triangle (pyramid) filled with hashtag symbols #.
# Let the height of the pyramid be determined by the user.

# Example
# Enter the height of the pyramid: 5
    #
   ###
  #####
 #######
#########


# Recommendation
# Don't forget that for us, a gap is an empty place, 
# and for Python, it's the same symbol as any other. 
# If you need to add an indentation, use
# space or tab character (\t).


('Задание 6. Треугольник из хештегов')

# Напишите программу, которая выводит на экран равнобедренный треугольник (пирамиду), заполненный символами хештега #.
# Пусть высоту пирамиды определяет пользователь.

# Пример
# Введите высоту пирамиды: 5
    #
   ###
  #####
 #######
#########


# Рекомендация
# Не забывайте, что для нас пробел — это пустое место, 
# а для Python — такой же символ, как и любой другой. 
# Если нужно добавить отступ, необходимо использовать
# пробел или символ табуляции (\t).

height_triangle = int(input("Укажите высоту пирамиды: "))
print()

for row in range(height_triangle):
    brick = 2 * height_triangle
    for col in range(brick):
        if col >= brick // 2 - row and col <= brick // 2 + row:
            print("#", end = "")
        else:
            print(" ", end = "")
    print()
