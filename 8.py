def calculate_taxi_payment(distance):
    тариф = 240
    за140м = 15
    distance_in_140m = distance * 1000 / 140
    additional_fare = за140м * distance_in_140m
    сумма = тариф + additional_fare
    return сумма
distance = int(input("введите расстояние в км. "))
payment = calculate_taxi_payment(distance)
print("Итоговая сумма оплаты", round((payment),1), "p.")
