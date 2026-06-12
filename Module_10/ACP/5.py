# Least Common Multiple (LCM)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


# -------- MENU --------
while True:
    print("\n====== LCM MENU ======")
    print("1. Find LCM of two numbers")
    print("2. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("LCM is:", lcm(a, b))

    elif choice == 2:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")