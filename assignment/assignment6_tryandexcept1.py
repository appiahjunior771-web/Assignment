
# Task 1: Create variables and print type
def task1():
    try:
        integer_var = 10
        float_var = 3.14
        string_var = "Hello"
        boolean_var = True

        print(integer_var, type(integer_var))
        print(float_var, type(float_var))
        print(string_var, type(string_var))
        print(boolean_var, 

type(boolean_var))
    except Exception as e:
        print(f"Error in Task 1: {e}")


# Task 2: Type conversions
def task2():
    try:
        # a
        float_num = 19.99
        int_num = int(float_num)
        print(int_num, type(int_num))

        # b

        integer_num = 50
        string_num = str(integer_num)
        print(string_num, type(string_num))

        # c
        string_num2 = "50"
        float_num2 = float(string_num2)
        print(float_num2, type(float_num2))
    except Exception as e:
        print(f"Error in Task 2: {e}")


# Task 3: Greeting message
def task3():
    try:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        print(f"Hello, {first_name} {last_name}!")
    except Exception as e:
        print(f"Error in Task 3: {e}")


# Task 4: Fixing the concatenationerror


def task4():
    try:
        age = 20
        # Fixed: convert int to str before concatenating
        print("You are " + str(age) + " years old.")
    except Exception as e:
        print(f"Error in Task 4: {e}")


# Task 5: Repeat favorite word
def task5():
    try:

        fav_word = input("Enter your favourite word: ")
        times = int(input("How many times should I repeat it? "))
        print((fav_word + " ") * times)
    except Exception as e:
        print(f"Error in Task 5: {e}")


# Main function to run all tasks
def main():
    task1()
    task2()

    task3()
    task4()
    task5()


# Run program
if __name__ == "__main__":
    main()
