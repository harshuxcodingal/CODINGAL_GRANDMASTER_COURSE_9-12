# Prime Check + Prime Sieve + Love Message

# -------- PRIME CHECK --------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# -------- SIEVE OF ERATOSTHENES --------
def prime_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    primes = []
    for i in range(n + 1):
        if sieve[i]:
            primes.append(i)

    return primes


# -------- MENU --------
while True:
    print("\n====== MENU ======")
    print("1. Check Prime Number")
    print("2. Prime Sieve")
    print("3. Love Message 💖")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        num = int(input("Enter number: "))
        if is_prime(num):
            print("Prime Number ✔")
        else:
            print("Not a Prime ❌")

    elif choice == 2:
        n = int(input("Generate primes up to: "))
        print("Prime Numbers:", prime_sieve(n))

    elif choice == 3:
        print("\n💖 Love you 3000 💖")

    elif choice == 4:
        print("Goodbye 💖 Stay awesome!")
        break

    else:
        print("Invalid choice! Try again.")