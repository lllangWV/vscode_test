def process_circle_data(radius_input):
    # Validate input
    if not isinstance(radius_input, (int, float)) or radius_input <= 0:
        print("Error: The radius must be a positive number.")
        return

    # Calculate area
    area = 3.14159 * radius_input ** 2

    # Calculate circumference
    circumference = 2 * 3.14159 * radius_input

    # Print results
    print(f"Circle with radius {radius_input}:")
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
    return area, circumference