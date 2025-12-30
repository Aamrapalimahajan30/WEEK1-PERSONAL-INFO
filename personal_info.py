# Personal Information Manager
# Author: Aamrapali Mahajan
# Description: Beginner Python project

print("\n" + "=" * 30)
print(" PERSONAL INFORMATION MANAGER ")
print("=" * 30)

# Static information
name = "Aamrapali"
age = 21
city = "Pune"
hobby = "Reading"

# User input
food = input("\nEnter your favourite food: ").strip()
while food == "":
    print("Input cannot be empty!")
    food = input("Enter your favourite food: ").strip()

color = input("Enter your favourite colour: ").strip()
while color == "":
    print("Input cannot be empty!")
    color = input("Enter your favourite colour: ").strip()

game = input("Enter your favourite game: ").strip()
while game == "":
    print("Input cannot be empty!")
    game = input("Enter your favourite game: ").strip()

# Calculation
age_months = age * 12

# Output
print("\n" + "-" * 30)
print(" YOUR DETAILS ")
print("-" * 30)

print(f"Name          : {name}")
print(f"Age           : {age} years")
print(f"Age (Months)  : {age_months}")
print(f"City          : {city}")
print(f"Hobby         : {hobby}")

print("\nPreferences:")
print(f"Favourite Food   : {food.capitalize()}")
print(f"Favourite Colour : {color.capitalize()}")
print(f"Favourite game   : {game.capitalize()}")

print("\nThank you for using the program!")
