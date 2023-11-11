breath = int (input ("enter the breath of your shape: "))
length = int (input ("enter the length of your shape: "))
if length == breath:
    shape = "square"

else:
    shape = "rectangle"

print (f"This shape is {shape}.")