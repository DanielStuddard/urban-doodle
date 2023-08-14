#!/user/bin/env python3
#Author: DanielStuddard

# This program calculates the area of a rectangle
# based on user input for length and width.

# defines how to find the area of a rectangle
def calculate_rectangle_area(length,width):
    return length * width

# requesting user input for length and width of rectangle then calculating the area
def main():
    print("Welcome to the Rectangle Area Calculator!")
    length = float(input("Enter the length of the rectangle:  "))
    width = float(input("Enter the width of the rectangle:  "))
    area = calculate_rectangle_area(length,width)
    print(f"The area of the rectangle is:  {area}")

# calls the def main
if __name__ == "__main__":
    main()

