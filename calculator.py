import math

what_to_do = input("Shall we do permutation or combination? Type p or c: ")
what_to_do = what_to_do.strip()
if what_to_do not in ["p", "c"]:
    print("Please enter either p or c.")
    exit()

try:
    n = int(input("Enter the total number of objects (n): ").strip())
    r = int(input("Enter the number of objects selected (r): ").strip())
except ValueError:
    print("Input Error. Input must be a number.")
    exit()

if n <= 0:
    print("Input Error. Input n must be 1 or above")
    exit()
elif r > n:
    print("Input Error. Input r must be less than or equal to n.")
    exit()
elif r <= 0:
    print("Input Error. Input r must be greater than 0.")
    exit()

if what_to_do == "p":
    print(int(math.factorial(n) / math.factorial((n - r))))
if what_to_do == "c":
    print(math.factorial(n) / (math.factorial(r) * math.factorial((n - r))))
