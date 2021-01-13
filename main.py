from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string, pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = [sym for sym in string.punctuation if sym not in ('"', "'")] # remove quotation marks

    password_letters = [choice(letters) for letter in range(randint(8, 10))]

    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if website == '' or email == '' or password == '':
        messagebox.showinfo(title='Oops!', message='Empty fields present')
    else:

        # message box
        # is_ok = messagebox.askokcancel(title=website, message=f'Details entered:\n website: {website}\n Email: {email}\n Password: {password}\n\n Is it ok to save?')
        # if is_ok:

        try:
            with open('data.json', 'r') as file:
                # file.write(f'{website} | {email} | {password}\n')

                # read old data
                data = json.load(file)

        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # update old data with new data
            data.update(new_data)  # update

            with open('data.json', 'w') as file:
                # write / save the updated data
                # indent makes it legible. # write
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            # email_username_entry.delete(0, END) # I rather save my email
            password_entry.delete(0, END)



# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='no data available')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            # print(website, email, password)

            messagebox.showinfo(title=website, message=f'website: {website}\n email: {email}\n password: {password}')
        else:
            messagebox.showinfo(title=f'{website}', message=f'{website} not found.')


        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('PyPass: password manager')
window.config(padx=10, pady=10)
window.resizable(False, False)


canvas = Canvas(width=100, height=100, highlightthickness=0)

# background
# bg_img = PhotoImage(file='assets/bg_00.png')
# bg_label = Label(window, image=bg_img) 
# bg_label.place(x=0, y=0)

# logo
logo_img = PhotoImage(file='assets/logo.png')
canvas.create_image(50, 50, image=logo_img)
canvas.grid(column=1, row=0)


# website row
website_label = Label(text='website')
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, padx=2.5, pady=2.5)
website_entry.config(highlightbackground='#eeeeee', highlightthickness=.5)
website_entry.focus()

search_btn = Button(text='search', width=13, command=search_password)
search_btn.grid(column=2, row=1)


# email/usernae row
email_username_label = Label(text='email / username')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, padx=2.5, pady=2.5)
email_username_entry.config(highlightbackground='#eeeeee', highlightthickness=.5)
email_username_entry.insert(0, 'parchment@gmx.com')


# password row
password_label = Label(text='password')
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, padx=2.5, pady=2.5)
password_entry.config(highlightbackground='#eeeeee', highlightthickness=.5)

password_btn = Button(text='generate password', command=generate_password)
password_btn.grid(column=2, row=3)


# add row
add_btn = Button(text='add', width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()