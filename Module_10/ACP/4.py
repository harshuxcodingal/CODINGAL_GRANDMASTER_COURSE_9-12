# Binary to Decimal Converter

def binary_to_decimal(binary):
    decimal = 0
    power = 0

    # read from right to left
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal


# -------- MENU --------
while True:
    print("\n====== BINARY MENU ======")
    print("1. Binary to Decimal")
    print("2. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        binary = input("Enter binary number: ")
        
        # basic validation
        if not all(bit in "01" for bit in binary):
            print("Invalid Binary Number ❌")
        else:
            print("Decimal Value:", binary_to_decimal(binary))

    elif choice == 2:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")