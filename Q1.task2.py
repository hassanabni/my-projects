breath = float (input ("enter the breath of your shape: "))
length = float (input ("enter the length of your shape: "))

if breath == length:
    shape = "square"
    area = int(2 * breath)
    perimeter =int (4 * length)

else:
    shape = "rectangle"
    area = int(length * breath)
    perimeter = int(2 * (length + breath))

    print(f"The {shape} has Perimeter: {perimeter} and Area: {area}")