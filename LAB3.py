a_ = int(input('Enter number X: '))
b_ = int(input('Enter number Y: '))
c_ = int(input('Enter number Z: '))

list_ = [a_, b_, c_]
unique_list = []
# create list of unique elements

for i in list_:
    if i not in unique_list:
        unique_list.append(i)
print(f'There are {len(unique_list)} unique numbers in {(a_, b_, c_)} = {unique_list}')


2)
zeros_ = []
for i in range(5):
    s_ = int(input('enter number: '))
    if s_ == 0:
        zeros_.append(s_)
if len(zeros_) == 0:
    print("массив чисел не включает нуль")
else:
    print(f'в массивах чисел есть {len(zeros_)} нули')

 3)
n_ = int(input('введите натуральное число'))
for i in range(n_):
    list_ = list(range(1,i +2))
    print(*list_, sep= '')

        #Или
n_ = int(input('введите натуральное число'))
for i in range(n_):
    
    print(*range(1,i+2), sep='')

 4)
n_ = int(input('введите натуральное число: '))
for i in range(n_):
    tb = list(range(1,i+1))
    t_ = sorted(tb,reverse=True)
    for j in range(n_-i-1):
        print(' ', end='')
    print(*range(1,i+2), sep='', *t_)
