
EXERCISE 2

a_ = int(input('Enter number X: '))
b_ = int(input('Enter number Y: '))

if a_ < b_:
    print(f"{a_} is smaller than {b_}")
elif a_ == b_:
    print(f'{a_} is equal to {b_}')

else:
    print(f'{b_} is smaller than {a_}')

# EXERCISE 3
a_ = int(input('Enter number X: '))
b_ = int(input('Enter number Y: '))
c_ = int(input('Enter number Z: '))


# function to get the greatest number from input
def greatest_number(x, y, z):
    maximum_ = max(x, y, z)
    return maximum_


if a_ == b_ == c_:
    print('The numbers you entered are EQUAL')
else:
    func_ = greatest_number(a_, b_, c_)
    print(func_, "is the greatest")

    # EXERCISE 4

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
