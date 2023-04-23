import tkinter


def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text='Label 1', font=("Arial", 24))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
my_button = tkinter.Button(text="Click me fast!", command=button_clicked)
my_button.grid(column=1, row=1)

my_button1 = tkinter.Button(text="Click!")
my_button1.grid(column=2, row=0)

# Entry component
my_input = tkinter.Entry(width=10)
print(my_input.get())
my_input.grid(column=3, row=2)




window.mainloop()
