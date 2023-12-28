A = int(input("введите длину прямоугольника A: "))
B = int(input("введите ширину прямоугольника B: "))
C = int(input("введите длину стороны квадрата C: "))
count = 0
while A >= C:
    A-= C
    B1 = B
    while B1>= C:
        B1 -= C 
        count += 1
print(count)
