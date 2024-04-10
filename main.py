import tkinter.messagebox
from tkinter import *
import random
# --------------UI------------------------


window = Tk()
window.minsize(height=600, width=600)
window.config(padx=50, pady=50)

# image canvas
canvas = Canvas(width=200, height=200)  # Adjust canvas size
image = PhotoImage(file="logo.png")  # Provide the complete file path
canvas.create_image(100, 100, image=image)  # Adjust image coordinates
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

# website text
website_field = Entry(width=53)
website_field.grid(row=1, column=1, sticky="w")
website_field.focus()

# email label
email_label = Label(text="Email :")
email_label.grid(column=0, row=2)

# email text
email_field = Entry(width=53)
email_field.grid(row=2, column=1, sticky="w")
email_field.insert(0, "np968738@gmail.com")

# password label
password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

# password text
password_field = Entry(width=28)
password_field.grid(row=3, column=1, sticky="w")

# ------------Password Generate-----------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_gen_button():
    password_list = []
    for char in range(1, 5):
        password_list.append(random.choice(letters))

    for char in range(1, 5):
        password_list += random.choice(symbols)

    for char in range(1, 5):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    password_field.insert(0, password)

    # copy to clipboard
    import pyperclip
    pyperclip.copy(password)


# password_generate button
password_button = Button(text="Generate Password", width=20, command=pass_gen_button)
password_button.grid(row=3, column=1, sticky="e")


# add function
def on_click():
    website_name = website_field.get()
    email_text = email_field.get()
    password_text = password_field.get()
    # ------------Pop up warning message------------
    if website_name == "" or email_text == "" or password_text == "":
        tkinter.messagebox.askokcancel(title="Warning Message", message="Insert All the Details", type="okcancel")
    # --------------Add Data to file----------
    else:
        file = open("password.txt", "a")
        file.write(f"{website_name}  ||  {email_text}  ||  {password_text}\n")
        file.close()


# add button button
add_button = Button(text="ADD", width=45, command=on_click)
add_button.grid(row=4, column=1, sticky="w")

window.mainloop()
