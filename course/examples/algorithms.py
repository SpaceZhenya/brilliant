"""Примеры алгоритмов: от псевдокода к Python"""

# Псевдокод:
#   ФУНКЦИЯ find_max(числа):
#       макс = числа[0]
#       ДЛЯ КАЖДОГО n ИЗ числа:
#           ЕСЛИ n > макс:
#               макс = n
#       ВЕРНУТЬ макс

def find_max(numbers):
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


# Псевдокод:
#   ФУНКЦИЯ contains(список, цель):
#       ДЛЯ КАЖДОГО x ИЗ список:
#           ЕСЛИ x == цель:
#               ВЕРНУТЬ Истина
#       ВЕРНУТЬ Ложь

def contains(lst, target):
    for x in lst:
        if x == target:
            return True
    return False


# Псевдокод:
#   ПОКА (balls exist):
#       move forward

def move_balls(balls):
    while balls > 0:
        print(f'Balls left: {balls}')
        print('move forward')
        balls -= 1
    print('Done!')


# Демонстрация
if __name__ == '__main__':
    print('find_max([3, 7, 2, 9, 1]):', find_max([3, 7, 2, 9, 1]))
    print('contains([1,2,3], 3):', contains([1, 2, 3], 3))
    print('contains([1,2,3], 9):', contains([1, 2, 3], 9))
    print()
    move_balls(3)
