import customtkinter
from modified_project import *
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry('700x350')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome to Mastermind", font=('Roboto', 20))
label.pack(pady=12, padx=10)

label_2 = customtkinter.CTkLabel(master=frame, text=f"You have {TRIES} tries to guess the color combinations", font=('Roboto', 15))
label_2.pack(pady=12, padx=10)

label_3 = customtkinter.CTkLabel(master=frame, text=("Valid colors are", COLORS), justify=customtkinter.RIGHT)
label_3.pack(pady=12, padx=10)

root.mainloop()