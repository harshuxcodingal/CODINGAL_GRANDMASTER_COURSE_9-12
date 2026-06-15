# Distribution
print("Dice Distribution")

for i in range(1, 7):
    print("P(X =", i, ") =", 1/6)

# Coin CDF
print("\nCoin CDF")
print("P(X <= Head) =", 0.5)
print("P(X <= Tail) =", 1.0)

# Rain Expectation
rain = [0, 10, 20]
prob1 = [0.2, 0.5, 0.3]

rain_expectation = 0

for i in range(len(rain)):
    rain_expectation += rain[i] * prob1[i]

print("\nExpected Rainfall =", rain_expectation)

# Expected Calls
calls = [0, 1, 2, 3]
prob2 = [0.1, 0.3, 0.4, 0.2]

call_expectation = 0

for i in range(len(calls)):
    call_expectation += calls[i] * prob2[i]

print("Expected Calls =", call_expectation)