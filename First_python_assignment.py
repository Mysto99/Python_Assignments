def square():
	length = int(input("Length: "))
	width = int(input("Width: "))
	perimeter = 2*(length+width)
	area = length*width
	print("Perimeter:", str(perimeter), "Area:", str(area))

def cube():
	length = int(input("Length: :"))
	width = int(input("Width: "))
	height = int(input("Height: "))
	volume = length*width*height
	area = 2*(length*width)+2*(length*height)+2*(width*height)
	print("Volume:", str(volume), "Area:", str(area))

def circle():
	radius = int(input("Radius: "))
	area = 3.14*(radius**2)
	circ = 2*3.14*radius
	print("Area:", str(area), "Circumference:", str(circ))

def sphere():
	radius = int(input("Radius: "))
	area = 4*3.14*(radius**2)
	volume = 0.75*3.14*(radius**3)
	print("Area:", str(area), "Volume:", str(volume))

choice = input("Choose a shape: ")
choice = choice.lower()

if choice == "square":
	square()
elif choice == "cube":
	cube()
elif choice == "circle":
	circle()
elif choice == "sphere":
	sphere()
else:
	print("Not Valid")