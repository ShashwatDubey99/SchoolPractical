def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2    

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def main():
    print('''Select An Operator To Perform The Operation
        '+' For Addition 
        '-' For Subtraction
        '*' For Multiplication
        '/' For Division''')
    operator = input('Enter Operator: ')
    num1 = int(input('Enter Number1: '))
    num2 = int(input('Enter Number2: '))
    if operator == '+':
        print(add(num1,num2))
    elif operator == '-':
        print(sub(num1,num2))
    elif operator == '*':
        print(mul(num1,num2))
    elif operator == '/':
        print(div(num1,num2))
    else:
        print('Invalid Operator')
main()

