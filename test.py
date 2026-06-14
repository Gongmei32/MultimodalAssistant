# ==========================================
# 1. VARIABLES AND DATA TYPES
# ==========================================
# Python automatically detects the data type. No need to declare it!

name = "Alice"          # String (text)
age = 25                # Integer (whole number)
height = 5.6            # Float (decimal)
is_student = True       # Boolean (True/False)

print("--- Data Types ---")
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


# ==========================================
# 2. BASIC MATH OPERATORS
# ==========================================
a = 10
b = 3

print("\n--- Math Operations ---")
print(f"Addition: {a + b}")       # 13
print(f"Division: {a / b}")       # 3.3333...
print(f"Floor Division: {a // b}") # 3 (divides and rounds down)
print(f"Modulo: {a % b}")         # 1 (remainder of 10 divided by 3)


# ==========================================
# 3. CONDITIONAL STATEMENTS (if/elif/else)
# ==========================================
# Python uses indentation (spaces/tabs) instead of curly braces {}

print("\n--- Conditionals ---")
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# ==========================================
# 4. LISTS (Arrays) AND LOOPS
# ==========================================
# A list stores multiple items in a single variable
fruits = ["apple", "banana", "cherry"]

print("\n--- Loops ---")
# 'for' loop: Iterates over a sequence
for fruit in fruits:
    print(f"I like eating {fruit}")

# 'while' loop: Runs as long as a condition is true
countdown = 3
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1  # Decrements countdown by 1


# ==========================================
# 5. FUNCTIONS
# ==========================================
# Use the 'def' keyword to create a reusable block of code

print("\n--- Functions ---")
def greet_user(username):
    """This function greets the user passed in as a parameter."""
    return f"Hello, {username}! Welcome to Python."

# Call the function and print the result
greeting_message = greet_user(name)
print(greeting_message)