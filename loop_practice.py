# Get a number and convert it to an int type
n = int(input('enter a number: '))
sum = 0
# count from 1 to n
for x in range(1,n):
    sum = sum + x
# output summation 1-n
print(f'sum from 1 to {n} is {sum}')
