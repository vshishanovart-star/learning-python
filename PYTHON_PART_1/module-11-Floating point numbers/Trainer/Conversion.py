'Conversion'

# When paying for purchases with a card abroad, banks convert through an intermediate currency. For example, if you pay with a domestic card for goods in euros, then this amount is first converted into dollars, and then into rubles.

# What needs to be done

# Write a program that receives the purchase price in euros as input, and then outputs the response in rubles. Let's imagine that we live in an alternate reality where 1 euro = 1.25 dollars, and 1 dollar = 60.87 rubles.

# Example

# cost_euro = 25

# At the exit

# Cost in rubles: 1902.1875

# What is being evaluated

#     The output result matches the condition.

#     The output contains a description of the result (the output numbers are accompanied by a text description).

'Конвертация'

# При оплате покупок картой за рубежом банки делают конвертацию через промежуточную валюту. Например, если оплачивать отечественной картой товар в евро, то сначала эта сумма конвертируется в доллары, а потом — в рубли.

# Что нужно сделать

# Напишите программу, которая получает на вход стоимость покупки в евро, а затем выводит ответ в рублях. Представим, что мы живём в альтернативной реальности, где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рубля.

# Пример

# cost_euro = 25

# На выходе

# Стоимость в рублях: 1902.1875

# Что оценивается

#     Результат вывода соответствует условию.

#     Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

# ---------------------------------------------------------------------------------------------

cost_euro = float(input("Введите стоимость покупки в валюте 'euro': "))
cost_dollars = cost_euro * 1.25
cost_rubles = cost_dollars * 60.87
print("Стоимость в рублях:", round(cost_rubles, 2))