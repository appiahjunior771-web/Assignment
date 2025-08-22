
# Task 1
# a. Create variables of different types
my_integer = 10
my_float = 3.14
my_string = "Hello, World!"
my_boolean = True

# b. Print each variable with its type
print("Integer:", my_integer, "Type:", type(my_integer))
print("Float:", my_float, "Type:", type(my_float))
print("String:", my_string, "Type:", type(my_string))

print("Boolean:", my_boolean, "Type:", type(my_boolean))


# Task 2
# a. Convert float to integer
float_value = 19.99
int_value = int(float_value)
print("Converted to Integer:", int_value, "Type:", type(int_value))

# b. Convert integer to string
integer_value = 50
string_value = str(integer_value)

print("Converted to String:", string_value, "Type:", type(string_value))

# c. Convert string to float
string_number = "50"
float_number = float(string_number)
print("Converted to Float:", float_number, "Type:", type(float_number))

# Task 3
# a. Take the user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# b. Print a greeting message
print("Hello, " + first_name + " " + last_name + "!")

# Task 4
# Given code with an error:
# age = 20
# print("You are " + age + " years old.")  # This causes an error

# a. Fix the error by converting the integer to a string
age = 20
print("You are " + str(age) + " years old.")

# b. Why did the error happen?
# Explanation:
# In Python, you cannot combine (concatenate) a string with an integer directly using '+'
# You must convert the integer to a string first using str().
# Task 5
# a. Ask the user for their favourite word
word = input("Enter your favourite word: ")

# b. Ask how many times to repeat it
times = int(input("How many times do you want to repeat it? "))

# c. Print the word that many times, separated by spaces
print((word + " ") * times)
