# ============================================
# DAY 1 — Functions & File I/O
# ============================================

# 1. BASIC FUNCTION
def greet(name):
    return f"Hello, {name}! Welcome to your Data Engineering journey."

print(greet("Vignesh"))

# 2. FUNCTION WITH MULTIPLE PARAMS
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

print(f"BMI: {calculate_bmi(70, 1.75)}")

# 3. DEFAULT PARAMETERS
def introduce(name, role="Data Engineer"):
    return f"I am {name}, aspiring {role}."

print(introduce("Vignesh"))
print(introduce("Vignesh", "Cloud Engineer"))

# 4. *args — multiple arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(10, 20, 30, 40))

# 5. **kwargs — keyword arguments
def display_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_profile(name="Vignesh", city="Chennai", goal="Data Engineer")

# 6. FILE I/O — Writing to a file
with open("output.txt", "w") as f:
    f.write("Name: Vignesh\n")
    f.write("Goal: Data + Cloud Engineer\n")
    f.write("City: Chennai\n")

print("File written successfully!")

# 7. FILE I/O — Reading from a file
with open("output.txt", "r") as f:
    content = f.read()
    print("\n--- File Contents ---")
    print(content)