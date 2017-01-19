##Smallest multiple
##Problem 5
##2520 is the smallest number that can be divided by
##each of the numbers from 1 to 10 without any remainder.
##
##What is the smallest positive number that
##is evenly divisible by all of the numbers from 1 to 20?

def sm(n):
    for i in range(n, factorial(n) + 1, n):
        if multiple(i, n):
            return i
    return -1

def multiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

def factorial(n):
    if n > 1: return n * factorial(n - 1)
    elif n >= 0: return 1
    else: return -1

print (sm(20))
