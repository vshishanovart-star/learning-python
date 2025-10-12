# """
# We were given an order to write a program for an electronic queue. Each person
# in the queue has a number: zero, first, second, third, and so on. Every hour,
# the queue decreases by one person, that is, the zero number leaves first, then
# the first, second, and so on. Our program receives one number as input — the
# number of people in the queue — and displays the queue service history on the
# screen: which numbers were left at what hour.
# """

# """
# Нам дали заказ написать программу для электронной очереди. У каждого человека в
# очереди есть номер: нулевой, первый, второй, третий и так далее. Каждый час
# очередь уменьшается на одного человека, то есть уходит сначала нулевой номер,
# затем первый, второй и так далее. Наша программа получает на вход одно число —
# количество людей в очереди — и выводит на экран историю обслуживания очереди:
# какие номера в какой час оставались.
# """

people = int(input("Введите кол-во людей в очереди: "))
print()
for hour in range(people + 1):
    print(hour, "час в очереди")
    if hour == people:
        print("Очередь обслужена!")
        break
    print("Номера людей в очереди:")
    for num in range(hour, people):
        print(num)
    print()
