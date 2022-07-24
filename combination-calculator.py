import math

def fact(n):
    return(math.factorial(n))
def fact(r):
    return(math.factorial(r))

def combination(n, r):
  fact(n)/fact(r)fact((n - r))

n = input("Enter the total number of objects/n in the set: ")
r = input("Enter the number of objects chosen/r in the set: ")

if n <= 0:
    print("Input Error. Input n must be 1 or above")
    break
elif r > n:
    print("Input Error. Input r must be less than or equal to n.")
elif r <= 0:
    print("Input Error. Input r must be greater than 0.")

else combination(n, r)
