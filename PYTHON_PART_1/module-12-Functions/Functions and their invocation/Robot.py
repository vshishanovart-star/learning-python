'Task 1. The robot'

# In one hotel, for an experiment, they want to put a robot at the entrance that will ask passersby if they would like to come in. If the answer is "Yes", the robot should greet the person and let them into the hotel. We wrote such a program for the robot using the function:

# Def greeting()
#  print('Hi!')
# print('Welcome!')
 

# while True:
#     a = input('Will you come in? Yes/No: ')
#     if a = 'Yes':
#     greeting
#     print('Next.\n')

# However, the programmer was in a hurry and made several mistakes.

# Copy the program to the replica, find and fix the errors. Make sure that the program is working correctly.

'Задача 1. Робот'

# В одном отеле для эксперимента на вход хотят поставить робота, который будет спрашивать у прохожих, не желают ли они зайти. При ответе «Да» робот должен приветствовать человека и пустить в отель. Для робота написали вот такую программу с использованием функции:

# Def greeting()
#  print('Привет!')
# print('Добро пожаловать!')
 

# while True:
#  a = input('Зайдёте? Да/Нет: ')
#  if a = 'Да':
#    greeting
#  print('Следующий.\n')

# Однако программист очень торопился и допустил несколько ошибок.

# Скопируйте программу в реплит, найдите и исправьте ошибки. Убедитесь, что программа работает корректно.

# -------------------------------------------------------------------------------------------------------

def greeting():
    print('Привет!')
    print('Добро пожаловать!')


while True:
    a = input('Зайдёте? Да/Нет: ')
    if a == 'Да':
        greeting()
    print('Следующий.\n')

