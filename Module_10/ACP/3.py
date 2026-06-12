# Recurrence Relations Demo

def factorial(n):
    # T(n) = T(n-1) + O(1)
    if n == 0:
        return 1
    return n * factorial(n - 1)


def show_recurrence():
    print("\n--- RECURRENCE RELATION ---")
    print("Factorial Recurrence:")
    print("T(n) = T(n-1) + O(1)")
    print("T(n) = T(n-2) + O(1) + O(1)")
    print("T(n) = T(n-3) + O(1) + O(1) + O(1)")
    print("Final: O(n) time complexity\n")


def expand_example(n):
    print("\n--- EXPANSION TRACE ---")
    for i in range(n, 0, -1):
        print(f"T({i}) -> T({i-1}) + O(1)")
    print("Base case reached!\n")


# -------- MENU --------
while True:
    print("\n====== RECURRENCE MENU ======")
    print("1. Show Recurrence Relation")
    print("2. Expansion Example")
    print("3. Factorial using Recursion")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        show_recurrence()

    elif choice == 2:
        n = int(input("Enter n: "))
        expand_example(n)

    elif choice == 3:
        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")