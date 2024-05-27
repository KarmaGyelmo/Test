print("Newton's Second Law of Moyion")
print("-----------------------------------")

# Determine the missing value
print("Select the missing value")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option number for the missing value: ")

#Prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter force (F) "))
    m = F / a
    print(f"Mass (m) = {m}")
