import random
import string

# Combine letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Password length
length = 8

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)