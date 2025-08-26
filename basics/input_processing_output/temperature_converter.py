SCALING_FACTOR = 9 / 5

OFFSET_VALUE = 32

temperature_in_celcius = float(input('Input your temperature in Celcius, C: '))

temperature_in_fahrenheit = (temperature_in_celcius * SCALING_FACTOR) + OFFSET_VALUE

print('Your temperature in Fahrenheit , will be: ', temperature_in_fahrenheit)


