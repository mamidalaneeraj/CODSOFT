print('welcome to python calculator')
print('----------------------------') 

# taking input of 2 numbers
a=float(input('enter the first number '))
b=float(input('enter the second number '))

# choosing the operand
print(' choose 1-addition  2-subtraction  3-multiplication  4-division')
choice=int(input('enter your choice '))

# doing required operations
if choice==1:
    print(f'the addition of {a} and {b} is {a+b}')
elif choice==2:
    print(f'the subtraction of {a} and {b} is {a-b}')
elif choice==3:
    print(f'the multiplication of {a} and {b} is {a*b}')
elif choice==4:
    if b==0:
        print('Error!division by zero is not possible') 
    else:
        print(f'the division of {a} and {b} is {a/b}')
else:
    print('invalid choice! please enter valid choice')