celsius = int(input("Please input a degree in celsius: \n>>>> "))
fahrenheit = int(input("Please input a degree in fahrenheit: \n>>>> "))

def celsius_to_fahrenheit(celsius):
    #program to convert celsius to fahrenheit
    fah = celsius * 9/5 + 32
    return fah

def fahrenheit_to_celsius(fahrenheit):
    cel = (fahrenheit - 32) * 5/9
    return cel

fah = celsius_to_fahrenheit(celsius)
cel = fahrenheit_to_celsius(fahrenheit)

print(f"{celsius} is {fah} in Fahrenheit.")
print(f"{fahrenheit} is {cel} in Celsius.")