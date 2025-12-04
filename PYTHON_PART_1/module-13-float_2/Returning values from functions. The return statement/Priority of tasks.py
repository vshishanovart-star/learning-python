'Task 3. Priority of tasks'

# In one data center, resources are distributed in such a way that large tasks are processed first, and then small ones. Each of these tasks is, in fact, just a huge stream of numbers. Your task, as the programmer of this center, is to write a program that will help determine which of the tasks needs to be solved first. 

# A sequence of N numbers is entered. You need to determine the number of the number with the most digits and display the corresponding message on the screen. If the number is negative, then count it as 0. To count the number of digits, implement the numeral_count function.

# ------------------------------------

'Задача 3. Приоритет задач'

# В одном дата-центре ресурсы распределены так, что сначала обрабатываются крупные задачи, а затем уже идут небольшие. Каждая из этих задач, по сути, просто огромный поток цифр. Ваша задача, как программиста этого центра, написать программу, которая поможет определять, какую из задач нужно решать в первую очередь. 

# Вводится последовательность из N чисел. Нужно определить номер числа, у которого больше всего цифр, и вывести на экран соответствующее сообщение. Если число отрицательное, то считать его за 0. Для подсчёта количества цифр реализуйте функцию numeral_count.

# -------------------------------------

def numeral_count(number):
    if number < 0:
        number = 0
    return len(str(number))


n = int(input("Введите кол-во задач: "))

longest_number = 0

for i in range(n):
    current_number = int(input("Введите число: "))
    if numeral_count(current_number) > numeral_count(longest_number):
        longest_number = current_number

print("Первая задача на обработку:", longest_number)




