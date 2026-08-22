# Write a python program using function to convert Celsius to Fahrenheit.

# c/5 = (f-32)/9
# c = 5 * (f-32)/9

def temp(f):
    return 5 * (f-32)/9

f = int(input("Enter the Temperature in F: ")) 


c = temp(f)
print(f"{round(c,2)}°C") # round: Rounds off upto 2 decimal values





