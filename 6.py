N = int(input("Введите целое число N: ")) 

result = 1 

while result < N:
    result *= 3

if result == N:
    print(True) 
else:
    print(False) 