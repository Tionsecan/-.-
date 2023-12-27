from math import ceil
 
def Оплата(d):
    return base+ceil(d/140)*add
 
base = 240
add = 15
distance = int(input("Введите расстояние: "))
print('Стоимость поездки: ', Оплата(distance))