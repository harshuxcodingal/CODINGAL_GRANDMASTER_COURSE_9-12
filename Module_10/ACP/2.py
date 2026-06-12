# Loop Time Complexity Demo

def o1():
    print("\n--- O(1) ---")
    arr = [10, 20, 30]
    print("First element:", arr[0])   # constant time


def on():
    print("\n--- O(n) ---")
    arr = [1, 2, 3, 4, 5]
    
    for i in arr:   # runs n times
        print(i)


def on2():
    print("\n--- O(n^2) ---")
    arr = [1, 2, 3]

    for i in arr:
        for j in arr:
            print(i, j)   # nested loop


# -------- MENU --------
while True:
    print("\n====== LOOP TIME MENU ======")
    print("1. O(1) Time")
    print("2. O(n) Time")
    print("3. O(n^2) Time")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        o1()

    elif choice == 2:
        on()

    elif choice == 3:
        on2()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")