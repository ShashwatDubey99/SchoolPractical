def Pal(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
def Arms(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = 0
    for digit in num_str:
       armstrong_sum += int(digit) ** num_digits
    return num == armstrong_sum

def main():
    print('''Press 1 For Checking No Palindrome
Press 2 For Checking No Armstrong
Press 3 For Exit''')
while True: 
    main()
    choice = int(input('Enter Your Choice: '))  
    if choice == 1: 
        num = int(input('Enter Number: '))
        if Pal(num):
            print(f'{num} is Palindrome')
        else:
            print(f'{num} is not Palindrome')
    if choice == 2:
        num = int(input('Enter Number: '))
        if Arms(num):
            print(f'{num} is Armstrong')
        else:
            print(f'{num} is not Armstrong')
    if choice == 3:
        break            
