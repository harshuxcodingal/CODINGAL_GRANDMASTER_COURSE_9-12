# Palindrome Number + GCD in one program

# -------- PALINDROME --------
def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse


# -------- GCD --------
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# -------- MENU --------
while True:
    print("\n====== MENU ======")
    print("1. Palindrome Number")
    print("2. GCD of Two Numbers")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter a number: "))
        if is_palindrome(n):
            print("Palindrome Number ✔")
        else:
            print("Not a Palindrome ❌")

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD is:", gcd(a, b))

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")