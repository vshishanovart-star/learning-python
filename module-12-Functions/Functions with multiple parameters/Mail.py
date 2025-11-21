"""Task 2. Mail 2

The rules have changed a bit at the post office: now you need to specify your last name, first name, country of residence, city, street, house number and apartment number in the postal notification.

Implement a function that receives all this data and displays it on the screen. In the program, call the function three times with different argument values.


Hint: seven arguments.

-------------------------------------

Задача 2. Почта 2

На почте немного поменялись правила: теперь в почтовом извещении нужно указывать фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.

Реализуйте функцию, которая получает все эти данные и выводит на экран. В программе вызовите функцию три раза с разными значениями аргументов.


Подсказка: семь аргументов.

----------------------------------------"""

def notification(surname, name, country_residence, sity, street, number_house, number_flate):
    print('ПОЧТОВОЕ_ИЗВЕЩЕНИЕ')
    print('Фамилия:', surname)
    print('Имя:', name)
    print('Страна проживания:', country_residence)
    print('Город:', sity)
    print('Улица:', street)
    print('Номер дома:', number_house)
    print('Номер квартиры:', number_flate)
    print()

notification('Шишанов', 'Вадим', 'Россия', 'Воркута', 'Гоголя', '6', '69')
notification('Габдиянова', 'Альбина', 'Узбекистан', 'Янгиюль', 'Адолат', '40-А', 'Квартиры нет, это частный дом')
notification('Имайкина', 'Венера', 'Россия', 'село Береговое', 'Заречная', '26', 'Квартиры нет, это частный дом')