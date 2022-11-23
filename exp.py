#Exponential function

import math

x = float(input('Write the value of x: '))
n = int(input('Write the repetitions of n: '))

#This function is used to calculate the factorial starting with 1
def my_fact_function(n):
    factorial = 1
    if n!=0:
        for i in range(1, n+1):
            factorial = factorial*i
#This loop will add the numbers to be multiplied.
#For example let's suppose that n=4, means that in each cycle add 1 until reaching n
# => 1*2*3*4 = 24 (the factorial of 4 is 24)
        return factorial

#Math.exp returns E raised to the power of x 
print ('x is: ',math.exp(x))
print ('n is: ',my_fact_function(n))

#conclusion of my logic: I have used the function math.exp to calculate the x power n of the formula.
#I have used the loop to calculate the factorial (n!) of the formula.