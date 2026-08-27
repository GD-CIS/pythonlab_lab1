import math

#Function to truncate decimal places because I don't like long decimals
def short_deci(value, n):
    value *= 10 ** n
    value = math.floor(value)
    value /= 10 ** n
    return value


#Area of a circle with radius of 5, should equal 78.539
circle = (math.pi * 5 ** 2)
print(short_deci(circle, 3))
#Volume of sphere with a radius of 3, should be 113.097
sphere = (4/3 * math.pi * 3 ** 3)
print(short_deci(sphere, 3))
#Hypotenuse of a right angled triangle with sides 3 and 4, should equal 5
print(int(math.sqrt(3 ** 2 + 4 ** 2)))

#Length of my name
name = "Gage Dorough"
print(len(name) - 1)

#My name but uppercase
print(name.upper())

#My name but lowercase
print(name.lower())

#BMI
height = 6 * 12
pounds = 210
print(type(height))
print(type(pounds))
BMI = pounds // height * 703
print(BMI)