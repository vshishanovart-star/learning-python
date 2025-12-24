'The "Eggs" task'

# As part of the Mars colonization program, Space Engineering has developed a special breed of turtles that are supposed to reproduce by laying eggs in the Martian soil.

# It is dangerous to lay eggs too close to the surface due to radiation, and too deep due to ground pressure and lack of oxygen. In general, there are a lot of factors, but experts have done a lot of work and suggested that the danger level for turtle eggs is calculated using the formula:

    
#                                         D = x^3 - 3x^2 - 12x + 10       

#  ;

# where x is the masonry depth in meters, and D is the hazard level in conventional units.

# To test the hypothesis, you need to take a soil sample at a safe depth, according to the formula.
# What needs to be done

# Write a program that finds the value of the depth x, at which the danger level is as close to zero as possible. The maximum allowable deviation of the hazard level from zero is given to the input program, and the program must calculate an approximate value of x that satisfies this deviation. It is known that the depth is exactly more than zero and less than four meters.

# An example of how the program works

# Enter the maximum allowable hazard level: 0.01

# Approximate depth of safe masonry: 0.732421875

# When you are ready, click the button below to see the solution to the problem.

# -------------------------------------------------------------------------------

'Задача «Яйца»'

# В рамках программы колонизации Марса компания «Спейс Инжиниринг» вывела особую породу черепах, которые по задумке должны размножаться, откладывая яйца в марсианском грунте.

# Откладывать яйца слишком близко к поверхности опасно из-за радиации, а слишком глубоко — из-за давления грунта и недостатка кислорода. Вообще, факторов очень много, но специалисты проделали большую работу и предположили, что уровень опасности для черепашьих яиц рассчитывается по формуле:

# ‌    
#                                         D = x^3 - 3x^2 - 12x + 10        

# ‌ ;

# где x — глубина кладки в метрах, а D — уровень опасности в условных единицах.

# Для тестирования гипотезы нужно взять пробу грунта на безопасной, согласно формуле, глубине.
# Что нужно сделать

# Напишите программу, находящую такое значение глубины х, при котором уровень опасности как можно более близок к нулю. На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля, а программа должна рассчитать приблизительное значение х, удовлетворяющее этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх метров.

# Пример работы программы

# Введите максимально допустимый уровень опасности: 0.01

# Приблизительная глубина безопасной кладки: 0.732421875

# Когда будете готовы, нажмите кнопку ниже, чтобы посмотреть решение задачи.

# ------------------------------------------------------------------------------

def danger(left, right):
    middle = (left + right) / 2
    middle_danger = middle ** 3 - 3 * middle ** 2 - 12 * middle + 10
    return middle, middle_danger


def calculation_safe_depth(max_danger):
    lower_bound = 0
    upper_bound = 4
    while True:
        mid, danger_level = danger(lower_bound, upper_bound)
        if danger_level > 0:
            lower_bound = mid
        else:
            upper_bound = mid
        if abs(danger_level) < max_danger:
            return mid

max_level_danger = float(input("Введите максимально допустимый уровень опасности: "))
result = calculation_safe_depth(max_level_danger)
print("Приблизительная глубина безопасной кладки", result, "метра")