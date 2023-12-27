def hypotenuse(first_leg, second_leg):
    return(round((first_leg ** 2 + second_leg ** 2) ** 0.5, 2))
    
first_leg = float(input("введите длину первого катета: "))
second_leg = float(input("введите длину второго катета: "))
print('гипотенуза равна:', hypotenuse(first_leg, second_leg))