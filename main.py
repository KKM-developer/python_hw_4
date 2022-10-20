#task_1
number_1 = float(input('Insert first number for division: '))
number_2 = float(input('Insert second number for division: '))
d = int(input('Insert how much numbers save after dot: '))
print(f'answer {round(number_1/number_2, d)}')

#task_2
some_number = int(input('Insert some number to found simple multipliers: '))
i = 2
simple_mult = []
while i * i <= some_number:
    while some_number % i == 0:
        simple_mult.append(i)
        some_number /= i
    i = i + 1
if some_number > 1:
    simple_mult.append(int(some_number))
print(simple_mult)

#task_3
from random import  randint as rnd
item = int(input('how much item in your list: '))
some_list = []
set_list = []
for _ in range(item):
    some_list.append(int(input('insert number: ')))
for elem in some_list:
    if elem not in set_list:
        set_list.append(elem)
print(some_list)
print(set_list)
#task_4
k = int(input('inset degree: '))
some_equation = ''
while k > 0:
    sign = rnd(0, 1)
    if sign == 0:
        sign = '-'
    else:
        sign = '+'
    some_equation += f'{rnd(0,100)}X^{k}{sign}'
    k-=1
some_equation+=f'{rnd(0,100)}=0'
print(some_equation)
