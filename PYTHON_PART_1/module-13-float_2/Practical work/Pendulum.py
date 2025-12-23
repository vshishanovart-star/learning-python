'Task 5. The pendulum'

# It is known that the amplitude of a swinging pendulum each time decays by 8.4% of the amplitude of the previous oscillation. If you swing a pendulum, then, strictly speaking, it will never stop, just the amplitude will constantly decrease until we consider such a pendulum to have stopped.
# What needs to be done

# Write a program that determines how many times the pendulum swings before it stops, in our opinion.

# The program receives as input the initial amplitude of the oscillation in centimeters and the final amplitude of the oscillation, which is considered the stop of the pendulum. Provide input control.

# Hint: To reduce the number, you can multiply it by a value that is less than one. For example, a decrease of 10%: 100 * 0.9 = 90.

# Example

# Enter the initial amplitude: 1

# Enter the stop amplitude: 0.1

# The pendulum is considered stopped after 27 oscillations.
# What is being evaluated

#     The output result matches the condition.
#     The output format corresponds to the example.
#     The output contains a description of the result (the output numbers are accompanied by a text description).

# -----------------------------------------------------------------------------------------------------------------


'Задача 5. Маятник'

# Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды предыдущего колебания. Если качнуть маятник, то, строго говоря, он не остановится никогда, просто амплитуда будет постоянно уменьшаться до тех пор, пока мы не сочтём такой маятник остановившимся.
# Что нужно сделать

# Напишите программу, определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход начальную амплитуду колебания в сантиметрах и конечную амплитуду колебаний, которая считается остановкой маятника. Обеспечьте контроль ввода.

# Подсказка: для уменьшения числа можно умножить его на значение, которое меньше единицы. Например, уменьшение на 10%: 100 * 0.9 = 90.

# Пример

# Введите начальную амплитуду: 1

# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний
# Что оценивается

#     Результат вывода соответствует условию.
#     Формат вывода соответствует примеру.
#     Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

# -------------------------------------------------------------------------------------------------

def fluctuations(start, finish):
    number_fluctuations = 0
    reducing_fluctuations = start
    while reducing_fluctuations > finish: 
        reducing_fluctuations *= 0.916
        number_fluctuations += 1
    return number_fluctuations


while True:
    initial_amplitude = float(input("Введите начальную амплитуду в сантиметрах: "))
    final_amplitude = float(input("Введите конечную амплитуду в сантиметрах: "))
    if initial_amplitude <= final_amplitude or initial_amplitude <= 0 or final_amplitude <= 0:
        print("Числовые значения должны быть положительными, не равными друг другу, а также начальное значение больше конечного\n")
    else:
        break

print("Маятник считается остановившимся через", fluctuations(initial_amplitude, final_amplitude), "колебаний")