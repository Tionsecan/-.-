def count_squares(A, B, C):
    count = 0
    while A >= C and B >=C:
        A-= C
        B-= C
        count += 1
    return count
A = int(input("Введите длину прямоугольника A: "))
B = int(input("Введите ширину прямоугольника B: "))
C = int(input("Введите длину стороны квадрата C: "))
print("Количество квадратов:", count_squares(A, B, C))