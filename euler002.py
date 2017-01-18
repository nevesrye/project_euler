##Even Fibonacci numbers
##Problem 2
##Each new term in the Fibonacci sequence is generated by adding the
##previous two terms. By starting with 1 and 2, the first 10 terms will be:
##
##1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##
##By considering the terms in the Fibonacci sequence whose values do not
##exceed four million, find the sum of the even-valued terms.

##f(n) = f(n-1) + f(n-2) where n>2
##f(1) = 1
##f(2) = 2

def fibo(n):
    if n == 1: # terminating case 1
        return 1
    elif n == 2: # terminating case 2
        return 2
    else:
        return fibo(n-1) + fibo(n-2)

# main

total = 0
i = 1
while fibo(i) <= 4000000:
    if fibo(i) % 2 == 0:
        total += fibo(i)
    i += 1
print(total)

