print('Welcome to this Calculator!!')
num1 = input('Please Enter First Number:')
while not num1.isnumeric():
    num1 = input('Please Enter Valid First Number:')
num1 = int(num1)
num2 = input('Please Enter Second Number:')
while not num2.isnumeric():
    num2 = input('Please Enter Valid Second Number:')
num2 = int(num2)

print(f'{num1} + {num2} = {num1+num2}')
print(f'{num1} - {num2} = {num1-num2}')
print(f'{num1} * {num2} = {num1*num2}')
print(f'{num1} / {num2} = {num1/num2}')
print(f'{num1} ^ {num2} = {num1**num2}')
print(f'{num1} % {num2} = {num1%num2}')