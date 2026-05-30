rowsCount = int(input("How many rows do you want? "))

for row in range(rowsCount):
    for star in range(row + 1):
        print("*", end=" ")
    print()