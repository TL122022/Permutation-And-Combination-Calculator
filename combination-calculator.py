import math

def fact(n):
    return(math.factorial(n))
def fact(r):
    return(math.factorial(r))

def combination(n, r):
  fact(n)/fact(r)fact((n - r))

n = input("Enter the total number of objects/n in the set: ")
r = input("Enter the number of objects chosen/r in the set: ")

combination(n, r)
