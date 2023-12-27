A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
 
count = B - A + 1
 
print(f"числа между {A} и {B} :")
for num in range(A, B + 1):
    print(num, end=" ")
print(f"\nВсего чисел между А и В: {count}")