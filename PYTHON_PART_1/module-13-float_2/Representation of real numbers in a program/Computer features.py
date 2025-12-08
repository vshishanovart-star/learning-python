'Task 1. Computer features'

# An IT company is testing the capabilities of various programming languages, compilers, and, of course, computers. The company has given you the task of figuring out which is the smallest possible number that can be obtained by constantly dividing the number by 2. Initially, the number is one. Also, in addition to the number itself, the company asks you to output the number of divisions. Implement such a program.

# --------------------------------------------------

'Задача 1. Возможности компьютера'

# В одной IT-компании тестируют возможности различных языков программирования, компиляторов и, конечно же, компьютеров. Компания дала вам задачу понять, какое самое маленькое возможное число можно получить путём постоянного деления числа на 2. Изначально число равно единице. Также, помимо самого числа, компания просит вывести количество делений. Реализуйте такую программу.

# --------------------------------------------------

x = 1
count_division = 0
while x != 0:
    x /= 2
    print(x)
    count_division += 1
print("Колличество делений:", count_division)