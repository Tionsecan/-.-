def convert_to_word(number):
    номера_слов = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать"
    }
    if number in номера_слов:
        return номера_слов[number]
    else:
        return ""

if __name__ == "__main__":
    while True:
        user_input = input("введите число от 1 до 12 ")
        try:
            number = int(user_input)
            if 1 <= number <= 12:
                word = convert_to_word(number)
                if word:
                    print(f"Число {number} - {word}")
                break
            else:
                print(" введите число ")
        except ValueError:
            print("введите подходящее число.")

