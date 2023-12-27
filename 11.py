def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    user_input = input("введите целое число: ")
    try:
        number = int(user_input)
        if is_prime(number):
            print(f"число {number} простое")
        else:
            print(f"число {number} не простое")
    except ValueError:
        print("нужно ввести ЦЕЛОЕ число")
