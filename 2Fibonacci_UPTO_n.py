def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(b)
(fib(int(input("Enter the number Upto which you want to print Fibonacci Series: "))))  