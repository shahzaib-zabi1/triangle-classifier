def classify_triangle(a, b, c):
    """
    Classifies a triangle based on its three side lengths.
    Checks for validity, then determines if it is equilateral, isosceles, or scalene.
    """
    # Check for valid triangle using the triangle inequality theorem
    if not (a + b > c and a + c > b and b + c > a):
        return "Not a valid triangle"

    # Check for triangle type
    if a == b and b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


if __name__ == "__main__":
    print("Enter the three side lengths of the triangle.")
    try:
        side1 = float(input("Enter side 1: "))
        side2 = float(input("Enter side 2: "))
        side3 = float(input("Enter side 3: "))

        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            print("Error: Side lengths must be positive.")
        else:
            result = classify_triangle(side1, side2, side3)
            print(f"The triangle is: {result}")

    except ValueError:
        print("Error: Please enter valid numbers for the side lengths.")
