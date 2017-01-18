##Multiples of 3 and 5
##Problem 1
##If we list all the natural numbers below 10 that are multiples of 3 or 5,
##we get 3, 5, 6 and 9. The sum of these multiples is 23.
##Find the sum of all the multiples of 3 or 5 below 1000.

# sum = 0 # sum is reserved for function and should not be interchangably used

total = 0
n = 1
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        total = total + n # total += n
    n = n + 1 # n += 1
print(total)
        
