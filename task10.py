# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random

n=int(input('Введите количество монеток: '))
eagle = 0
tail = 0
print(f"{n} ->", end=' ')
while n > 0:
    coin = random.randint(0, 1)
    n -= 1
    if coin > 0:
        eagle +=1
    else:
        tail += 1
    print(f"{coin}", end=' ')

print()   
if eagle > tail:
    print(f"{tail}")
else:
    print(f"{eagle}")