"""
Project: 2

Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.

You decide to host your application on servers running in the cloud. You pick a hosting provider

that charges $0.51 per hour. You will launch your service using one server and want to know

how much it will cost to operate per day,per week,per month.

Write a Python program that displays the answers to the following questions:

How much does it cost to operate one server per day?

How much does it cost to operate one server per week?

How much does it cost to operate one server per month?

How many days can I operate one server with $918?
"""
# Cost of running one server per hour in dollars
costPerHour = 0.51

# Calculating costs
costPerDay = costPerHour * 24
costPerWeek = costPerDay * 7
costPerMonth = costPerDay * 30

# Given budget in dollars
userBudget = 918
numberOfDaysWithBudget = userBudget / costPerDay

# Displaying the results
print("Cost to operate one server per day: $", round(costPerDay, 2))
print("Cost to operate one server per week: $", round(costPerWeek, 2))
print("Cost to operate one server per month: $", round(costPerMonth, 2))
print("With $918, you can operate one server for", int(numberOfDaysWithBudget), "days")
