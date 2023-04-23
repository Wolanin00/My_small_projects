import tkinter


def miles_to_km():
    miles = int(miles_input.get())
    km = round(miles * 1.609344)
    result_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(pady=20, padx=20)

# Miles textbox
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is equal label
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Result label
result_label = tkinter.Label(text='0')
result_label.grid(column=1, row=1)

# Km label
km_label = tkinter.Label(text='Km')
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = tkinter.Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
