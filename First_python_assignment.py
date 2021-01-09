from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Calculator")

def clear():
	select.grid_forget()
	square_button.grid_forget()
	cube_button.grid_forget()
	circle_button.grid_forget()
	sphere_button.grid_forget()

def square():
	clear()
	Label(root, text="Enter the dimensions: ").grid(row=0, column=0, columnspan=2)
	Label(root, text="Length: ").grid(row=1, column=0)
	Label(root, text="Width: ").grid(row=2, column=0)
	length = Entry(root).grid(row=1, column=1)
	width = Entry(root).grid(row=2, column=1)
	calculate = Button(root, text="Calculate").grid(row=2, column=2)
	length = length.get()
	width = width.get()
	perimeter = 2*(length + width)
	area = length*width
	Label(root, text=str(perimeter)).grid(row=3, column=0)
	Label(root, text=str(area)).grid(row=4, column=0)

def cube():
	clear()

def circle():
	clear()

def sphere():
	clear()



select = Label(root, text="Select a shape:")
select.grid(row=0, column=0, columnspan=2)

square_button = Button(root, text="Square", command=square)
square_button.grid(row=1, column=0)

cube_button = Button(root, text="Cube", command=cube)
cube_button.grid(row=1, column=1)

circle_button = Button(root, text="Circle", command=circle)
circle_button.grid(row=1, column=2)

sphere_button = Button(root, text="Sphere", command=sphere)
sphere_button.grid(row=1, column=3)

root.mainloop()