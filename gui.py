import customtkinter

# Main class initiation stuff
class App(customtkinter.CTk): 
    def __init__(self):
        super().__init__()

        # Layout of the main app
        self.title("Music recommender")
        self.geometry("1920x1080")
        self.grid_columnconfigure(0, weight=1)




# Definition of the recommendation list
class ScrollableList(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        
        # creates the list in the frame for the parsed values 
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)




app = App()
app.mainloop()