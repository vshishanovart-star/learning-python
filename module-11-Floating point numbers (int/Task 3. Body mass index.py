'Task 3. Body mass index'

# Alexey works as a nutritionist in a private clinic. Every day he sees patients of different ages and with different height (in meters) and weight (in kg). For each person, he needs to calculate the body mass index - this is weight divided by height squared. According to government standards, the index is rounded to two digits after the dot. Then, according to this index, it is determined whether everything is in order for a person with body weight: if up to 18.5, then there is a shortage; up to 25, everything is fine, up to 30 there is already an excess, and after 30, obesity. Write such a program for Alexey.


'Задача 3. Индекс массы тела'

# Алексей работает диетологом в частной клинике, каждый день он принимает пациентов разных возрастов и с разными показателями роста (в метрах) и веса (в кг). Для каждого человека ему нужно считать индекс массы тела - это вес поделить на рост в квадрате. По государственным стандартам индекс округляется до двух знаков после точки. Затем по этому индексу определяется, всё ли в порядке у человека с массой тела: если до 18.5, то недобор; до 25 - всё нормально, до 30 уже идёт избыток, а после 30 - ожирение. Напишите такую программу для Алексея.


'Decision'

weight = float(input("Введите вес пациента: "))
height = float(input("Введите рост пациента: "))
print()

bmi = round(weight / height ** 2, 2)
print("Индекс массы тела равен:", bmi)
if bmi < 18.5:
    print("У пациента недобор массы тела")
elif bmi < 25:
    print("У пациента нормальная масса тела")
elif bmi < 30:
    print("У пациента избыток массы тела")
else:
    print("У пациента ожирение") 