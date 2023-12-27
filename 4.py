A = int(input("Введите число А"))
B = int(input("Введите число Б"))

sum_all = 0 
sum_even = 0 
sum_odd = 0 

for num in range(A, B+1): 
    sum_all += num 
    if num % 2 == 0: 
        sum_even += num 
    else:
        sum_odd += num 

print("Сумма всех чисел:", sum_all) 
print("Сумма четных чисел:", sum_even) 
print("Сумма нечетных чисел:", sum_odd) 