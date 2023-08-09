def get_number_input(prompt, lower_limit, upper_limit):
    while True:
        try:
            num = int(input(prompt))
            if lower_limit <= num <= upper_limit:
                return num
            print("Invalid input. Please enter a number between {} and {}.".format(lower_limit, upper_limit))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Welcome to the Door Game!")
    door_choice = input("Choose a door: (red door / yellow door) ").lower()

    if door_choice == "red door":
        number_choice = get_number_input("Choose a number from 1 to 5: ", 1, 5)

        if number_choice in [1, 4]:
            numbers_list = []
            for i in range(3):
                num = get_number_input("Enter a number from 1 to 100: ", 1, 100)
                numbers_list.append(num)

            print("Your selected numbers:", numbers_list)
        else:
            print("You lost.")

    elif door_choice == "yellow door":
        number_choice = get_number_input("Choose a number from 6 to 10: ", 6, 10)

        if number_choice % 2 == 0:
            numbers_list = []
            for i in range(3):
                num = get_number_input("Enter a number from 1 to 100: ", 1, 100)
                numbers_list.append(num)

            print("Your selected numbers:", numbers_list)
        else:
            print("You lost.")

    else:
        print("Invalid choice. Please choose either red door or yellow door.")
        return

    if sum(numbers_list) > 130 and sum(numbers_list) < 1079:
        print("You win!")
    else:
        print("You lost.")


if __name__ == "__main__":
    main()


