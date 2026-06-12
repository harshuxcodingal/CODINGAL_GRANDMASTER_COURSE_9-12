# Strong Arms + Fact Message + Roman to Integer

def strong_arms():
    print("\n💪 STRONG ARMS MODE ACTIVATED!")
    print("Keep pushing... Strength is built, not given!")

def thats_a_fact():
    print("\n📢 THAT’S A FACT!")
    print("Hard work beats talent when talent doesn't work hard.")

def roman_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 0

    for char in reversed(s):
        value = roman[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    return total


# -------- MENU SYSTEM --------
while True:
    print("\n====== MAIN MENU ======")
    print("1. Strong Arms 💪")
    print("2. That's a Fact 📢")
    print("3. Roman to Integer 🔢")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        strong_arms()

    elif choice == 2:
        thats_a_fact()

    elif choice == 3:
        roman = input("Enter Roman Number (e.g. XIV, IX, MCM): ").upper()
        result = roman_to_int(roman)
        print("Integer Value:", result)

    elif choice == 4:
        print("Exiting... Stay Strong 💪")
        break

    else:
        print("Invalid choice! Try again.")