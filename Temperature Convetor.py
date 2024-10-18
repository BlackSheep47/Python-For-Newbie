# Temperature Convertor

unit = input("Enter the Temperature celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature: "))

if unit == "C":
    temp = (temp * 9) / 5 + 32
    unit = "°F"
    print(f"The Temperature is: {temp} {unit}")
elif unit == "F":
    temp = ((temp - 32) * 5) / 9
    unit = "°C"
    print(f"The Temperature is: {temp} {unit}")
else:
    print(f"{unit} is invalid unit")