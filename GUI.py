import customtkinter
from modified_project import *
import tkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.game_title = customtkinter.CTkLabel(self, text="Welcome to MasterMind",width=280, height= 40, 
        fg_color=("#4B7CE7", "#1E5CE1"), corner_radius=8, font=("Roboto", 23))
        self.game_title.pack(side="top", padx=20, pady=20)

        self.available_colors = customtkinter.CTkLabel(self, text="Available colors",width=100, height= 30, 
        fg_color="#41be47", corner_radius=8, font=("Roboto", 15), text_color="black")
        self.available_colors.pack(side="top", padx=20, pady=20)

        self.color_list = customtkinter.CTkLabel(self, text=COLORS, font=('Roboto', 15))
        self.color_list.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter guess combination", width=170, height=25, 
        border_width=2, corner_radius=0, justify='center')
        self.entry.place(relx=0.46, rely=0.5, anchor=tkinter.CENTER)

        self.button_1 = customtkinter.CTkButton(self, text="Submit", command=self.open_toplevel, width=90, height=25)
        self.button_1.place(relx=0.4, rely=0.62, anchor=tkinter.CENTER)

        # Storing the input of the user
        self.entry_value = self.entry.get()
        # Functions for events that the button were triggered
       
        def clear():
            self.entry.delete(0, len(self.entry_value)+1)
        
        def delete():
            self.entry.delete(len(self.entry_value)-1)

        self.clear = customtkinter.CTkButton(self, text="Clear", command=clear, width=90, height=25, 
        fg_color="red", hover=True, hover_color="gray")
        self.clear.place(relx=0.6, rely=0.62, anchor=tkinter.CENTER)
        
        self.delete = customtkinter.CTkButton(self, text="delete", command=delete, corner_radius=0, width=70, 
        height=25, border_width=1, fg_color="red", hover=True, hover_color="gray")
        self.delete.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x100")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

        # Integrating the modified project module
        self.game = game(self.entry_value)



if __name__ == "__main__":
    app = App()
    app.mainloop()