#Drawn_number
from time import sleep

from random import randint

print('Generating 5 numbers...')
sleep(1)
drawn_number = (randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5))
print(drawn_number)

print(f'The highest value was: {max(drawn_number)}')
print(f'The lowest value was: {min(drawn_number)}')