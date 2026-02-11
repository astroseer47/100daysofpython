from tkinter import *
import random
from tkinter import messagebox

from pandas.io.clipboard import clipboard_set

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

available_characters = [letters, numbers, symbols]

letters_count = 5
symbols_count = 3
numbers_count = 2


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    generated_password = []
    for count in range(0, letters_count):
        generated_password.append(random.choice(letters))

    for count in range(0, symbols_count):
        generated_password.append(random.choice(symbols))

    for count in range(0, numbers_count):
        generated_password.append(str(random.choice(numbers)))

    random.shuffle(generated_password)

    password = "".join(generated_password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    clipboard_set(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_url.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    new_entry = f"website:{website} | username:{username} | password:{password}"

    with open("./passwords.txt", "a") as file:
        file.write("\n")
        file.write(new_entry)

    website_url.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)


canvas = Canvas(window, width=200, height=200)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0,column=1)

website_url_label = Label(text="Website URL:")
website_url_label.grid(row=1, column=0)

website_url = Entry(name="website_url" , width=40)
website_url.grid(row=1,column=1,columnspan=2)



username_label = Label(text="Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(name="username_entry",width=40)
username_entry.grid(row=2,column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(name="password", width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_random_password)
password_button.grid(row=3,column=2)


add_button = Button(text="Add", command=save_password, width=38)
add_button.grid(row=4, column=1,columnspan=3)






window.mainloop()