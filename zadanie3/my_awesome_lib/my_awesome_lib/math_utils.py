def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    pi = 3.14159
    return pi * radius ** 2
