import customtkinter
from CTkListbox import *

# Main class initiation stuff
class App(customtkinter.CTk): 
    def __init__(self):
        super().__init__()

        # Layout of the main app
        self.title("Music recommender")
        self.geometry("860x520")
        self.grid_columnconfigure(0, weight=1)
        self.scrollable_checkbox_frame = ScrollableList(master=self, width=300, height=200, corner_radius=0)
        self.scrollable_checkbox_frame.grid(row=0, column=0, sticky="nsew", padx=(10,20), pady=(10, 0))







# Definition of the recommendation list
class ScrollableList(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text="new text")
        self.label.grid(row=0, column=0, padx=20)

        # list of items 
        






app = App()
app.mainloop()