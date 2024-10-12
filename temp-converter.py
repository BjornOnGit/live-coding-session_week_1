def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def temperature_converter():
    print("Temperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Choose a conversion option (1-4): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius)}")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"Temperature in Celsius: {fahrenheit_to_celsius(fahrenheit)}")
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Kelvin: {celsius_to_kelvin(celsius)}")
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"Temperature in Celsius: {kelvin_to_celsius(kelvin)}")
    else:
        print("Invalid option selected!")

temperature_converter()