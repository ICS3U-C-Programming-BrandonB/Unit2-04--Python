#!/usr/bin/env python3

# Created By: Brandon
# Date: October 1st, 2025
# This program asks the user for the radius, calculates area and circumference
# then displays the area and circumference of a circle

import constants
import math


# Takes input from user
def main():
    radius = float(input("Enter Radius of the Circle: (cm): "))

    # Calculates circumference and area of circle
    area = constants.PI * math.pow(radius, 2)
    circumference = constants.TAU * radius

    # Displays the circumference and area of the circle back to the user
    print("")
    print("Area = {:,.2f}(cm)".format(area))
    print("Circumference = {:,.2f}(cm)".format(circumference))


# Outputs the function
if __name__ == "__main__":
    main()
