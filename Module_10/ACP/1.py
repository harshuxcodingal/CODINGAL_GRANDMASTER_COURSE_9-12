# Multiply By N (Table Generator)

def multiply_by_n(n):
    print(f"\nMultiplication Table of {n}")
    print("------------------------")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# -------- MENU --------
while True:
    print("\n====== MENU ======")
    print("1. Multiply By N (Table)")
    print("2. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        multiply_by_n(num)

    elif choice == 2:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")