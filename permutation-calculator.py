import math

def fact(n):
    return(math.factorial(n))
def fact(n, r):
    return(math.factorial(n - r))

def permutation(n, r):
  fact(n)/fact((n - r))

n = input("Enter the total number of objects/n: ")
r = input("Enter the number of objects selected/r: ")

permutation(n, r)
