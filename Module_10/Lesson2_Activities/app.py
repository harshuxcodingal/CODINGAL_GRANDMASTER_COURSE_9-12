def o1_example():
    print("\n--- O(1) CONSTANT TIME ---")
    arr = [10, 20, 30, 40, 50]
    
    # Direct access (always same time)
    print("First element:", arr[0])
    print("Last element:", arr[-1])


def on_example():
    print("\n--- O(n) LINEAR TIME ---")
    arr = [1, 2, 3, 4, 5]
    
    total = 0
    for num in arr:
        total += num   # runs n times
    
    print("Sum of array:", total)


def on2_example():
    print("\n--- O(n^2) QUADRATIC TIME ---")
    arr = [1, 2, 3]
    
    print("All pairs:")
    for i in arr:
        for j in arr:
            print(i, j)   # nested loop → n * n


while True:
    print("\n====== TIME COMPLEXITY MENU ======")
    print("1. O(1) Example")
    print("2. O(n) Example")
    print("3. O(n^2) Example")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        o1_example()
    elif choice == 2:
        on_example()
    elif choice == 3:
        on2_example()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")