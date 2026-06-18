# ==================================
# RAIN EXPECTATIONS
# ==================================

rain = [0, 10, 20]
probability = [0.2, 0.5, 0.3]

expected_rain = 0

for i in range(len(rain)):
    expected_rain += rain[i] * probability[i]

print("Expected Rainfall =", expected_rain)