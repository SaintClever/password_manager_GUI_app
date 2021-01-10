from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('PyPass: password manager')
window.config(padx=20, pady=20)
window.resizable(False, False)


canvas = Canvas(width=200, height=200, highlightthickness=0)

# bg_img = PhotoImage(file='assets/bg_00.png')
# canvas.create_image(100, 100, image=bg_img)
# canvas.grid(column=0, row=0)

logo_img = PhotoImage(file='assets/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)



l = Label(text='hello')
l.grid(column=1, row=1)


window.mainloop()