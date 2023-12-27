K = int(input("Введите число K: "))
N = int(input("Введите число N: "))
if N < 0:
    print("N должно быть > 0")

result = N * K

print(f"{N} раз(а) по {K} это: {result}")