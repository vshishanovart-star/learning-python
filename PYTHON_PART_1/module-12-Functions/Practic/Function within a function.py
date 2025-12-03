"""Task 2. A function within a function
What needs to be done

Evgeny is taking a special programming test. Everything was going well until the hero came across the topic of "Functions". The task sounds like this:

The main branch of the program, not counting the function headers, consists of one line of code. This is a call to the test() function. It asks you to enter an integer. If it is positive, then the positive() function is called, the body of which contains the command to display the word "Positive" on the screen. If the number is negative, the negative() function is called, its body contains an expression for displaying the word "Negative" on the screen.

Help Evgeny and implement such a program.

Example 1
Enter a number: 5
Positive

Example 2
Enter a number: -4
Negative

--------------------------------

Задача 2. Функция в функции
Что нужно сделать

Евгений проходит специальный тест по программированию. Всё шло хорошо, пока герой не наткнулся на тему «Функции». Задание звучит так:

Основная ветка программы, не считая заголовков функций, состоит из одной строки кода. Это вызов функции test(). В ней запрашивается на ввод целое число. Если оно положительное, то вызывается функция positive(), тело которой содержит команду вывода на экран слова «Положительное». Если число отрицательное, то вызывается функция negative(), её тело содержит выражение вывода на экран слова «Отрицательное».

Помогите Евгению и реализуйте такую программу.

Пример 1
Введите число: 5
Положительное

Пример 2
Введите число: -4
Отрицательное

-----------------------------------"""

def test():
    integer_number = int(input("Введите любое целое число: "))
    if integer_number > 0:
        positive()
    elif integer_number < 0:
        negative()
            
def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

test()