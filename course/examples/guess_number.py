import random


def guess_number():
    secret = random.randint(1, 100)
    attempts = 0

    print('Я загадал число от 1 до 100. Угадай!')

    while True:
        try:
            guess = int(input('Твой вариант: '))
            attempts += 1

            if guess > secret:
                print('Меньше!')
            elif guess < secret:
                print('Больше!')
            else:
                print(f'Угадал за {attempts} попыток!')
                break
        except ValueError:
            print('Введи целое число!')


if __name__ == '__main__':
    guess_number()
