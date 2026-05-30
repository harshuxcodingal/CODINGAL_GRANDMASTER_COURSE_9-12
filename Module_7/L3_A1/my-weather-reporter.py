locationName = input("Enter your area name: ")
weatherDegree = float(input("Enter current temperature in Celsius: "))

if weatherDegree > 40:
    print("Heat Alert Issued!")

if weatherDegree > 28:
    print("The weather is pleasant for outdoor activities.")
else:
    print("You may need warm clothes today.")

if weatherDegree > 40:
    print("Condition: Extreme Heat")
elif weatherDegree > 30:
    print("Condition: Sunny")
elif weatherDegree > 20:
    print("Condition: Mild Weather")
else:
    print("Condition: Chilly Weather")

import datetime
import calendar

currentDateTime = datetime.datetime.now()

print("Location:", locationName)
print("Date & Time:", currentDateTime)

print(calendar.calendar(currentDateTime.year))