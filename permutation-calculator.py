import math

def fact(n):
    return(math.factorial(n))
def fact(n, r):
    return(math.factorial(n - r))

def permutation(n, r):
  fact(n)/fact((n - r))

n = input("Enter the total number of objects/n: ")
r = input("Enter the number of objects selected/r: ")

if n <= 0:
    print("Input Error. Input n must be 1 or above")
    break
elif r > n:
    print("Input Error. Input r must be less than or equal to n.")
elif r <= 0:
    print("Input Error. Input r must be greater than 0.")

else: permutation(n, r)
