def main():
    while True:
        try:
            temperature, unit = input("Enter a temperature and its unit (e.g., 25 C or 77 F):",).split(" ")
            if float(temperature) < -273.15 or float(temperature) > 6000:
                ''' Check if the temperature is within the valid range for physical temperatures.'''
                raise ValueError("Invalid temperature value")
            if unit != "C" and unit != "F":
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            if unit == "C":
                celsius_to_fahrenheit(temperature)
                break 
            elif unit == "F":
                fahrenheit_to_celsius(temperature)
                break 
        except Exception as e:
            print(e)

def celsius_to_fahrenheit(celsius):
    '''
    function `celsius_to_fahrenheit(celsius)` that takes a Celsius temperature as an argument 
    and returns the equivalent temperature in Fahrenheit. Use the formula `fahrenheit = (celsius * 9/5) + 32`.
    '''
    return print(f"Temperature in Fahrenheit: {round((float(celsius) * 9/5) + 32, 2)} F")

def fahrenheit_to_celsius(fahrenheit):
    '''
    function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature as an argument 
    and returns the equivalent temperature in Celsius. Use the formula `celsius = (fahrenheit - 32) * 5/9`.
    '''
    return print(f"Temperature in Celsius: {round((float(fahrenheit) - 32) * 5/9, 2)} C")

main()
                   

