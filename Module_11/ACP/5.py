# ==================================
# LONGEST CONSECUTIVE 1's
# ==================================

n = int(input("Enter a number: "))

count = 0
max_count = 0

while n > 0:
    if n & 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

    n = n >> 1

print("Longest Consecutive 1's =", max_count)