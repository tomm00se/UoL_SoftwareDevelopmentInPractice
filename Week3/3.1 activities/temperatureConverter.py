# Exercise: Write a program that converts temperatures from celsius to fahrenheit and vice versa

def convert_temperature(temp:float, unit:str) -> float:
    """
    This function converts temperature from celsius to fahrenheit and vice versa
    """
    if unit == "c":
        return (temp * 9/5) + 32
    elif unit == "f":
        return (temp - 32) * 9/5
    else:
        return "Invalid unit"
    
print(convert_temperature(0, "c")) # Output: 32.0
print(convert_temperature(32, "f")) # Output: 0.0