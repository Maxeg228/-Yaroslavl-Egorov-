from random import randint

rocks = randint(4, 30)
pl = 1
num = -1

print(f'В куче {rocks} камней')
while rocks > 0:
    if pl == 1:
        print('Ходит первый игрок')
        while not 1 <= num <= 3:
            try:
                num = int(input('Введите число от 1 до 3: '))
            except ValueError:
                pass
        rocks -= num
        num = - 1
        print(f'В куче {max((rocks, 0))} камней')
        pl = 2
        continue
    if pl == 2:
        print('Ходит второй игрок')
        while not 1 <= num <= 3:
            try:
                num = int(input('Введите число от 1 до 3: '))
            except ValueError:
                pass
        rocks -= num
        num = -1
        print(f'В куче {max((rocks, 0))} камней')
        pl = 1
        continue
else:
    if pl == 1:
        print('Выйграл второй игрок')
    if pl == 2:
        print('Выйграл первый игрок')
