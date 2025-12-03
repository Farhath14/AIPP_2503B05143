def area_rectangle(x, y):
    return x * y
def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x

AREA_FUNCTIONS = {
    "rectangle": lambda x, y=0: area_rectangle(x, y),
    "square": lambda x, y=0: area_square(x),
    "circle": lambda x, y=0: area_circle(x)
}

def calculate_area(shape, x, y=0):
    func = AREA_FUNCTIONS.get(shape)
    if func is None:
        raise ValueError("Invalid shape type")
    return func(x, y)

shape = input("Enter shape (rectangle/square/circle): ").lower()

if shape == "rectangle":
    x = float(input("Enter length: "))
    y = float(input("Enter width: "))
    print("Area:", calculate_area(shape, x, y))

elif shape in ["square", "circle"]:
    x = float(input("Enter side/radius value: "))
    print("Area:", calculate_area(shape, x))
else:
    print("Invalid shape")