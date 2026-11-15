def celsius_to_fahrenheit(c):
    """Convert a Celsius temperature to Fahrenheit."""
    return c * 9 / 5 + 32

for temp in [0, 25, 37, 100]:
    print(f"{temp}C = {celsius_to_fahrenheit(temp)}F")
