num = int(input("Enter a number: "))

original = num
sum_value = 0

digits = len(str(num))

while num > 0:
    digit = num % 10
    sum_value += digit ** digits
    num //= 10

if sum_value == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")