def factor(n):
    n = int(input('Enter an integer:'))
    for i in range(1, n+1):
        if n % 1 == 0:
            print(i)
factor(15)