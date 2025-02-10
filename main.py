import math

#Function to calculate the area of a circle
def area_of_circle(pi, radius):
    return pi * (radius ** 2)

#Function to calculate the total due after tax
def total_due(money, tax_rate):
    return money + (money * tax_rate)

#Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

#Test case 1: Area of a Circle
radius_1 = 10
print(f"Area of Circle with radius {radius_1}: {area_of_circle(math.pi, radius_1):.2f}")
radius_2 = 6
print(f"Area of Circle with radius {radius_2}: {area_of_circle(math.pi, radius_2):.2f}")
radius_3 = 24
print(f"Area of Circle with radius {radius_3}: {area_of_circle(math.pi, radius_3):.2f}")
radius_4 = 2
print(f"Area of Circle with radius {radius_4}: {area_of_circle(math.pi, radius_4):.2f}")
radius_5 = 1
print(f"Area of Circle with radius {radius_5}: {area_of_circle(math.pi, radius_5):.2f}")

#Test case 2: Taxes
money_1 = 20
tax_rate_1 = 0.06
print(f"Total due for ${money_1} with {tax_rate_1*100}% tax: {total_due(money_1, tax_rate_1):.2f}")
money_2 = 54
tax_rate_2 = 0.04
print(f"Total due for ${money_2} with {tax_rate_2*100}% tax: {total_due(money_2, tax_rate_2):.2f}")
money_3 = 68
tax_rate_3 = 0.08
print(f"Total due for ${money_3} with {tax_rate_3*100}% tax: {total_due(money_3, tax_rate_3):.2f}")

#Test case 3: Temperature conversion from Fahrenheit to Celsius
fahrenheit_1 = 32
print(f"{fahrenheit_1}°F is equal to {fahrenheit_to_celsius(fahrenheit_1):.5f}°C")
fahrenheit_2 = 80
print(f"{fahrenheit_2}°F is equal to {fahrenheit_to_celsius(fahrenheit_2):.4f}°C")
fahrenheit_3 = 73
print(f"{fahrenheit_3}°F is equal to {fahrenheit_to_celsius(fahrenheit_3):.5f}°C")
fahrenheit_4 = 42
print(f"{fahrenheit_4}°F is equal to {fahrenheit_to_celsius(fahrenheit_4):.5f}°C")
