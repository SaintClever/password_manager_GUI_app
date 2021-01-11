from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    with open('data.txt', mode='a') as file:
        file.write(f'\n{website} | {email} | {password}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('PyPass: password manager')
window.config(padx=10, pady=10)
window.resizable(False, False)


canvas = Canvas(width=200, height=200, highlightthickness=0)

# background
# bg_img = PhotoImage(file='assets/bg_00.png')
# bg_label = Label(window, image=bg_img) 
# bg_label.place(x=0, y=0)

# logo
logo_img = PhotoImage(file='assets/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# website row
website_label = Label(text='website')
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, padx=2.5, pady=2.5)
website_entry.config(highlightbackground='#eeeeee')
website_entry.focus()


# email/usernae row
email_username_label = Label(text='email / username')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, padx=2.5, pady=2.5)
email_username_entry.config(highlightbackground='#eeeeee')
email_username_entry.insert(0, 'parchment@gmx.com')


# password row
password_label = Label(text='password')
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, padx=2.5, pady=2.5)
password_entry.config(highlightbackground='#eeeeee')

password_btn = Button(text='generate password')
password_btn.grid(column=2, row=3)


# add row
add_btn = Button(text='add', width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)



window.mainloop()