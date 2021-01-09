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


choice = input("Choose a shape: ")

if choice == "square":
	square()
elif choice == "cube":
	cube()