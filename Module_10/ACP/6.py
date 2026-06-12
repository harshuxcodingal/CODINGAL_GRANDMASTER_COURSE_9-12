# 2-Digit Prime Numbers Program

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def two_digit_primes():
    print("\n--- 2-DIGIT PRIME NUMBERS ---")
    primes = []

    for num in range(10, 100):   # 2-digit range
        if is_prime(num):
            primes.append(num)

    print(primes)


# -------- MENU --------
while True:
    print("\n====== PRIME MENU ======")
    print("1. Check Prime Number")
    print("2. Show 2-Digit Primes")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter number: "))
        if is_prime(n):
            print("Prime ✔")
        else:
            print("Not Prime ❌")

    elif choice == 2:
        two_digit_primes()

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")