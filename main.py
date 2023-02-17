import customtkinter
from modified_project import *
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # setting the property of the main window
        self.geometry("500x400")
        self.maxsize(500, 400)
        self.minsize(500, 400)

        self.game_title = customtkinter.CTkLabel(self, text="Welcome to MasterMind",width=280, height= 40, 
        fg_color=("#C2FA6C"), corner_radius=8, font=("Roboto", 23), text_color="black")
        self.game_title.pack(side="top", padx=20, pady=20)

        self.available_colors = customtkinter.CTkLabel(self, text="Available colors",width=100, height= 30, 
        fg_color="#3BF885", corner_radius=8, font=("Roboto", 15), text_color="black")
        self.available_colors.pack(side="top", padx=20, pady=20)

        self.color_list = customtkinter.CTkLabel(self, text=COLORS, font=('Roboto', 15))
        self.color_list.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter guess combination", width=170, height=25, 
        border_width=2, corner_radius=0, justify='center')
        self.entry.place(relx=0.46, rely=0.5, anchor=tkinter.CENTER)

        # this for adding the game event when the user click the check button
        self.counter = 0
        def gameFunction():
            
            if  self.counter < TRIES:
                if self.entry.get() != "":
                    pass
                else: 
                    self.text_1.delete("0.0", "1000.0")
                    return self.text_1.insert("0.0", "Please Input first")
                
                self.result = game(self.entry.get())
                self.text_1.delete("0.0", "1000.0")
                self.text_1.insert("0.0", (self.result + "\n"))
                self.counter += 1
            else:
                self.text_1.delete("0.0", "1000.0")
                self.text_1.insert("0.0", (f"YOU LOSE!"))
                self.text_1.insert("0.0", (f"Sorry you reached the maximum TRIES of {TRIES}\n"))
                self.button_1.configure(state="disabled")
                self.retry.configure(state="normal")
                self.button_1.configure(state="disabled")
                self.entry.configure(state="disabled")
                self.delete.configure(state="disabled")

        # Other functions for events when the buttons are trigger
        def clear():
            if self.entry.get() == "":
                pass
            else:
                self.entry.delete(0, len(self.entry.get())+1)

        def retry():
            self.entry.configure(state="normal")
            self.entry.delete(0, len(self.entry.get())+1)
            self.result = game(self.entry.get())
            self.text_1.delete("0.0", "1000.0")
            self.button_1.configure(state="normal")
            self.delete.configure(state="normal")
            self.retry.configure(state="disabled")
            self.counter = 0
       

        self.button_1 = customtkinter.CTkButton(self, text="Check", command=gameFunction, width=90, height=25, fg_color="#3BF885",
        text_color="black", font=("Roboto", 13))
        self.button_1.place(relx=0.4, rely=0.62, anchor=tkinter.CENTER)


        self.retry = customtkinter.CTkButton(self, text="retry", command=retry, width=90, height=25, 
        fg_color="#FF2D00", hover=True, hover_color="gray", state="disabled", font=("Roboto", 13), text_color="black")
        self.retry.place(relx=0.6, rely=0.62, anchor=tkinter.CENTER)
        
        self.delete = customtkinter.CTkButton(self, text="clear", command=clear, corner_radius=0, width=70, 
        height=25, border_width=1, fg_color="#FF2D00", hover=True, hover_color="gray", font=("Roboto", 13), text_color="black")
        self.delete.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

        self.text_1 = customtkinter.CTkTextbox(self, width=300, height=75)
        self.text_1.place(relx=0.52, rely=0.8, anchor=tkinter.CENTER)


if __name__ == "__main__":
    app = App()
    app.mainloop()