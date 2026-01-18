import random

numbers = [random.randint(1, 50) for i in range(10)]
numbers_2 = [999, 999, 999]
numbers.extend(numbers_2)

print(numbers)