from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('PyPass: password manager')
window.config(padx=20, pady=20)
window.resizable(False, False)


canvas = Canvas(width=200, height=200, highlightthickness=0)

# background
# bg_img = PhotoImage(file='assets/bg_00.png')
# canvas.create_image(100, 100, image=bg_img)
# canvas.grid(column=0, row=0)

# logo
logo_img = PhotoImage(file='assets/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# website row
website_label = Label(text='website')
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)


# email/usernae row
email_username_label = Label(text='email / username')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)


# password row
password_label = Label(text='password')
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_btn = Button(text='generate password')
password_btn.grid(column=2, row=3)


# output row
output = Entry(width=36)
output.grid(column=1, row=4, columnspan=2)



window.mainloop()