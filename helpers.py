class InvalidInputError(Exception):
    pass


def choose_option(options):
    # TODO update to exception handle here for value that is out of range
    for index, option in enumerate(options):
        print(f"{index + 1}: {option}")

    num = get_user_selection("int")
    if num < 1 or num > len(options):
        print("\nYour selection was not a valid option")
        return choose_option(options)
    else:
        return num


def get_user_selection(inputType):
    while True:
        user_input = input(("\nPlease enter your selection: "))
        try:
            if not user_input:
                raise ValueError("\nInput can not be empty")

            if inputType == "int":
                if not user_input.isdigit():
                    raise InvalidInputError("\nPlease enter a valid value")

        except ValueError as err:
            print(err)
        except InvalidInputError as err:
            print(err)
        else:
            return user_input if inputType == "str" else int(user_input)
