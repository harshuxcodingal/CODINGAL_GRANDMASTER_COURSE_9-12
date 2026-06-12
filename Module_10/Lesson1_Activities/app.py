# One Algorithm - Three Faces (Iterations)
# Sum of first N numbers using For, While, and Recursion

# -------- INPUT --------
n = int(input("Enter a number: "))

print("\n--- ONE ALGORITHM: THREE ITERATIONS ---\n")

# -------- 1. FOR LOOP --------
total_for = 0
for i in range(1, n + 1):
    total_for += i

print("1. Using FOR loop:", total_for)

# -------- 2. WHILE LOOP --------
total_while = 0
i = 1

while i <= n:
    total_while += i
    i += 1

print("2. Using WHILE loop:", total_while)

def sum_recursive(x):
    if x == 0:
        return 0
    return x + sum_recursive(x - 1)

print("3. Using RECURSION:", sum_recursive(n))