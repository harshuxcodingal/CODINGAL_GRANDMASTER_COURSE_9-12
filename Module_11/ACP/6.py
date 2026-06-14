# ==================================
# ALL SUBSTRINGS
# ==================================

text = input("Enter a string: ")

n = len(text)

print("\nAll Substrings:")

for i in range(n):
    for j in range(i + 1, n + 1):
        print(text[i:j])