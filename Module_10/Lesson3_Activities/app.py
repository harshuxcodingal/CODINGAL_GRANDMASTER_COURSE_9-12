def factorial(n, depth=0):
    # Print call (this shows stack going DOWN)
    print("  " * depth + f"call: factorial({n})")

    if n == 0:
        print("  " * depth + "return 1")
        return 1

    result = n * factorial(n - 1, depth + 1)

    # Print return (this shows stack coming UP)
    print("  " * depth + f"return {result}")
    return result


# -------- MAIN --------
n = int(input("Enter a number: "))

print("\n--- CALL STACK TRACE ---\n")
answer = factorial(n)

print("\nFinal Result:", answer)