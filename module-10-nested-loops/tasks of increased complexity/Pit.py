'Task 2. The pit'

# Imagine that you are developing a computer game with text graphics. You have been assigned to create a landscape generator.


'Задача 2. Яма'

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта.


n = int(input("Введите число: "))
print()

num = n

for row in range(n):
    for col in range(n * 2):
        if col <= row:
            print(num, end = "")
            num -= 1
            if num == 0:
                num += 1
        elif col >= (n * 2 - row - 1):
            print(num, end = "")
            if num < n:
                num += 1
        else:
            print(" ", end = "")
            if col == n * 2 - row - 2:
                num += 1 
    print()

         
        
        
        
