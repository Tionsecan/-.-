a = int(input("Введите длину отрезка А: "))
b = int(input("Введите длину отрезка B: "))
while a >= b:
    a-=b
print("Длина незанятой части отрезка а",a)