# Show the UI
print("^.^ " * 21)
print("^.^ " * 3, " " * 58, "^.^ " * 3)
print("^.^ " * 3, "Advanced Calculator".center(58), "^.^ " * 3)
print("^.^ " * 3, " " * 58, "^.^ " * 3)
print("^.^ " * 21)
print(" " * 58)
# Welcome the user
print("Welcome to the Advanced Calculator!".center(58))
print("^.^ " * 13)
# Show the menu options
print("Menu Options:")
print("^.^ " * 13)
print("1. Celsius to Fahrenheit Conversion" .center(44))
print("2. Fahrenheit to Celsius Conversion".center(44))
print("^.^ " * 13)
# Get input from the user.
strMenu = input("Enter your choice: ")
# if the user chooses 1, go to C to F calc
if (strMenu == "1"):
    # ask for degrees C
    celsius = float(input("Enter the temperature in Celsius: "))
    # do calculation for C to F
    fahrenheit = (celsius * 9/5) + 32
    # Print conversion
    print(f"{celsius} degrees Celsius is equal to {fahrenheit:.1f} degrees Fahrenheit.")
# if the user chooses 2, go to F to C calc
elif (strMenu == "2"):
    # ask for degrees F
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    # do calculation for F to c
    celsius = (fahrenheit - 32) * 5/9
    # Print conversion
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.1f} degrees Celsius.")
else:
    print("Invalid Option")
