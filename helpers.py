def get_user_value_int():
    while True:
        try:
            return int(input(("Enter your selection: ")))
        except ValueError:
            print("Please enter a valid number")


def get_user_input_str(message):
    while True:
        try:
            return str(input((f"{message}: ")))
        except ValueError:
            print("An empty value is not allowed.")


def choose_option():
    options = ("View Tasks", "Add Task", "Edit Task", "Quit")
    for index, option in enumerate(options):
        print(f"{index + 1}: {option}")
    return get_user_value_int()
