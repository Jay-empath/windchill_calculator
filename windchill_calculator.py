
# Function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Function to calculate wind chill

def calculate_wind_chill(temp_f, wind_speed):
    wind_chill = 35.74 + (0.6215 * temp_f) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return wind_chill

# Ask user for temperature
temperature = float(input("What is the temperature? "))

# Ask for the unit
unit = input("Fahrenheit or Celsius (F/C)? ")

# Convert if needed
if unit.upper() == 'C':
    temperature = celsius_to_fahrenheit(temperature)

# Loop through wind speeds and print wind chill
for wind_speed in range(5, 65, 5):
    wind_chill = calculate_wind_chill(temperature,wind_speed)
    print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
