userNumber = int(input("Enter any number: "))

isPrime = True

if userNumber < 2:
    isPrime = False
else:
    for divisor in range(2, userNumber):
        if userNumber % divisor == 0:
            isPrime = False
            break

if isPrime:
    print(userNumber, "is Prime")
else:
    print(userNumber, "is Not Prime")