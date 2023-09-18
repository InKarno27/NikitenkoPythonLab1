"""
Лабораторная 1 Вариант 9
Написать функцию, которая принимает целочисленный список, состоящий из n элементов, и возвращает количество четных чисел в списке.
"""

numbers = []

while True:
    num = input()
    if num.lower() == "стоп":
        break

    try:
        number = int(num)

        if number % 2 == 0:
            numbers.append(number)

    except ValueError:
        print("Ошибка")

print("Четные числа:", numbers)
