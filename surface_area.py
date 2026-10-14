pi = 3.142
radius = float(input("Enter the radius of the sphere: "))
while radius < 0:
    radius = float(input("Please enter the radius of the sphere: "))
volume = (4/3) * pi * (radius * radius * radius)
surface_area = 4 * pi * (radius * radius)
print("The volume of the sphere is: ", volume)
print("The surface area of the sphere is: ", surface_area)
