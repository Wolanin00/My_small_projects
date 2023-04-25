import json
import string
import random
import pyperclip
from tkinter import *
from tkinter import messagebox

DEFAULT_EMAIL = 'day_29_project@gmail.com'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '*']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = []
    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])

    password = ''.join(password_list)
    random.shuffle(password_list)
    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(text=password)


# ---------------------------- FIND PASSWORD-------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=f"Password Info for: {website}", message=f"Credentials:\n"
                                                                               f"email: {data[website]['email']}\n"
                                                                               f"password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No items meeting the assumptions")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = website_entry.get().title()
    email_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text
        }
    }

    if len(website_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Info", message="Don't leave any fields empty! Please fill it!")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'a') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=158, height=158, highlightthickness=0)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(79, 79, image=my_pass_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=26)
website_entry.grid(column=1, row=1, sticky='W')
website_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(column=1, row=2, columnspan=2, sticky='W')
email_entry.insert(0, DEFAULT_EMAIL)
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3, sticky='W')

# Button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1, sticky='E')
generate_password_button = Button(text="Generate Password", width=15, command=password_generator)
generate_password_button.grid(column=2, row=3, sticky='E')
add_button = Button(text="Add", width=38, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='E')

window.mainloop()
