# Get input from the user
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# Convert age to an integer
try:
    age = int(age_str)
except ValueError:
    print("Invalid age entered. Please enter a number.")
    exit()

# Perform a simple calculation
years_to_100 = 100 - age

# Display the output
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"You will turn 100 in {years_to_100} years.")
