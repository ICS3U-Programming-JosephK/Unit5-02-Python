#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: November 25
# This program gets the user triangle's base and height and outputs the area


def calc_area(height, base):
    # Function definition with 2 parameters
    # This function receives data, calculates, then outputs

    # Calculate the are aof the triangle
    area = height * base / 2

    # Display the results (area) to the user
    print(f"\nThe area of your triangle is {area} cm²")


def main():
    # This function gets height and base, also does error checking

    # Asks the user for the height in decimals (cm)
    try:
        height_from_user = float(input("\nEnter Height (cm): "))

    # Exception thrown if the user did not enter a number
    except ValueError:
        input("You must enter a positive integer. Please try again.")

    # Check if the user is capable of entering a negative number
    if height_from_user < 0:
        print("You need to enter a positive number")

    # Else if, it is not the case, ask for the with
    elif height_from_user > 0:
        # Asks the user for the width in decimals (cm)
        try:
            width_from_user = float(input("\nEnter Width (cm): "))

        # Exception thrown if the user did not enter a number
        except ValueError:
            input("You must enter a positive integer. Please try again.")

        # Check if the user is capable of entering a negative number
        if width_from_user < 0:
            print("You need to enter a positive number")

        # Only if the user does not mess up the inputs, do you call the function
        else:
            # call functions
            # passing 2 arguments to each function
            calc_area(height_from_user, width_from_user)


if __name__ == "__main__":
    main()
