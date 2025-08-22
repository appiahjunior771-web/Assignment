
# Task 1: Convert string to lowercase
def task1(s):
    try:
        return s.lower()
    except Exception as e:
        return f"Error: {e}"

# Task 2: Swap case of string
def task2(s):
    try:
        return s.swapcase()
    except Exception as e:
        return f"Error: {e}"

# Task 3: Remove uppercase characters from string


def task3(s):
    try:
        return ''.join(char for char in s if not char.isupper())
    except Exception as e:
        return f"Error: {e}"

# Task 4: Count uppercase and lowercase characters in string
def task4(s):
    try:
        uppercase = sum(1 for char in s if char.isupper())
        lowercase = sum(1 for char in s if char.islower())

        return f"Uppercase: {uppercase}, Lowercase: {lowercase}"
    except Exception as e:
        return f"Error: {e}"

# Task 5: Remove non-alphabetic characters from string
def task5(s):
    try:
        return ''.join(char for char in s if char.isalpha())
    except Exception as e:
        return f"Error: {e}"
