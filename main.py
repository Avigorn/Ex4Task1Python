# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input("Введите первый элемент прогрессии: "))
difference = int(input("Введите разность прогрессии: "))
quantity = int(input("Введите количество элементов прогрессии: "))
progression = []
for i in range(quantity):
    ai = first_element + (i * difference) 
    progression.append(ai)
for j in progression:
        print(j)