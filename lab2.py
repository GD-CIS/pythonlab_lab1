import math

name = "Gage Dorough"
age = 23
height = 6.0
favorite_color = "Black"
circle_area = math.pi * 5 ** 2
#Multiple prints
print(name)
print(age)
print(height)
print(favorite_color)

#Single print
print(name, age, height, favorite_color)

#Formatted Text
print(f"My name is {name} and my favorite color is {favorite_color.lower()}!")

print(f"I'm {age:04d} years old")

print(f"I'm {age:b} years old, but in binary, which is cooler")

print(f"""
Height: {height}
Age: {age}
""")

print(f"{circle_area:.1f}")

print(math.sqrt(age))

print(math.sin(height), math.cos(height))

print(f"""
Sum: {age + 5}
Difference: {height -4}
Product: {age * height}
Quotient: {height / 2}
Remainder: {age % 3}
Exponent: {age ** 2}
""")

temp = int(input(f"What is the tempurature outside({u'\u2109'})?"))
celsius = (temp - 32) * 5/9
print(f"The temp outside in celsius is {round(celsius, 2)}({u'\u2103'})")


