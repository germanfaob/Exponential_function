x = float(input('Insert the value of x: '))
n = int(input('Insert the value of n: '))

def factorial(n):
    f=1
    if n==0:
        return 1
    elif n>0:
        for k in range(1,n+1):
            f=f*k
        return f

def exp(x):
    s=0
    for i in range(0,13):
        s=s+(x**i)/factorial(i)
    return s

print('The value of x: ',exp(x))
print('The value of n: ',factorial(n))