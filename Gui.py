from tkinter import *
app = Tk()
app.title("Window")
app.geometry('300x250')

#To print a text
greet = Label(app, text='Hello')
greet.grid(row=5, column=5)

# A function that is called when a button is clicked
def when_clicked():
    message = Label(app, text='The button was clicked')
    message.grid()

# To create a button
button = Button(app, text='Click me', command=when_clicked, fg='red', bg='yellow')
button.grid()

# To create an input field
e = Entry(app)
e.grid()

def my_click():
    my_label = Label(app, text="Hello " + e.get())
    my_label.grid()

my_button = Button(app, text='Enter your name', command=my_click)
my_button.grid()

# To keep the window open
app.mainloop()