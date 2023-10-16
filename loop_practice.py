# Get a number and convert it to an int type
n = int(input('enter a number: '))
sum = 0
# count from 1 to n
for x in range(1,n):
    sum = sum + x
# output summation 1-n
print(f'sum from 1 to {n} is {sum}')

#Get another number and convert it to an int type
a = int(input('enter another number: '))
factorial = 1
#count from 1 to n
for y in range(1,a):
    factorial = factorial * y
#Output the factorial (1 * 2 * 3 * 4 * ... * n)
print (f'The factorial from 1 to {a} is {factorial}')
