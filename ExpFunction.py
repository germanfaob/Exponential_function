#This function is used to calculate the factorial starting with 1
def factorial(n):
    f=1
    if n==0:
        return 1
    elif n>0:
        for k in range(1,n+1):
            f=f*k
        return f

#This function calculate the x.
#*Important: The second number of the range indicates the number of terms in the series.
#If the number is higher, the approximation to the number (e) is greater.
#You can modify the second number of the range to whatever you want to increase or decrease the approximation to (e)
def exp(x):
    s=0
    for i in range(0,13):
        s=s+(x**i)/factorial(i)
    return s

print('The value of x: ',exp(x))
print('The value of n: ',factorial(n))
