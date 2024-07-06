import random
def random_num():   # Ф-ция рандомного номера в диапазоне 1-100
    x = random.randrange(1, 101)
    return x
def number_check(number):   # Ф-ция проверка на цифру
    while True:
        if number.isdigit() and 0 < int(number) <= 100 or number == "stop" or number == "стоп":
            return number
        else:
            number = input("А может быть все-таки введем целое число от 1 до 100? Или stop/стоп, если хотите сдаться!:")

while True:
    print("Добро пожаловать в числовую угадайку")
    x_rnd = random_num()
    # print("Загаданное число:(test)", x_rnd)  # Для тестирования
    number = input("Угадаете число? Вы можете сдаться, написав слово: 'stop' или 'стоп'.\nВведите ваше число от 1 до 100: ")
    number = number_check(number)
    count_try = 1
    while True:
        if count_try > 3:
            print("Это была", count_try, "попытка, вы безнадежны, лучше сдайтесь =)")
        if number == "stop" or number == "стоп":
            print("Вы сдались!")
            break
        if int(number) > x_rnd:
            number = input("Слишком много, попробуйте еще раз: ")
            number = number_check(number)
            count_try += 1
        elif int(number) < x_rnd:
            number = input("Слишком мало, попробуйте еще раз: ")
            number = number_check(number)
            count_try += 1
        elif int(number) == x_rnd:
            print("Вы угадали с", count_try, "раза, поздравляем, это число", x_rnd)
            break
    again = input("Хотите начать игру заново?(да/нет): ")
    if again == "да" or again == "yes" or again == "lf":
        continue
    elif again == "нет" or again == "no" or again == "ytn":
        print("Рады были видеть вас в игре 'Угадайка 2024'. Заходите еще =)")
        break



