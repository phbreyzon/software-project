import customtkinter
from CTkListbox import *
import webbrowser
from functions import list_of_recommendations



        
        
        
# Main class initiation stuff
class App(customtkinter.CTk): 
    def __init__(self):
        super().__init__()
        
        # Layout of the main app
        self.title("Music recommender")
        self.geometry("860x520")
        self.grid_columnconfigure(0, weight=1)
        self.scrollable_checkbox_frame = Recommendations_list(master=self, width=300, height=200, corner_radius=10, values=["value1","value2","value3"])
        
        
        self.scrollable_checkbox_frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=(30, 10))
        self.entry = customtkinter.CTkEntry(master=self.scrollable_checkbox_frame, placeholder_text="Enter recommendation")
        self.entry.grid(row=0, column=0, padx=20, pady=20)
        
        
        
        button = customtkinter.CTkButton(master=self.scrollable_checkbox_frame, text="recommend",command=lambda : list_of_recommendations(self.entry.cget("state"),5))
        button.grid(row=1, column=1, padx=20, pady=20)
    

        
        
        











# Definition of the recommendation list
class Recommendations_list(customtkinter.CTkScrollableFrame):
    def __init__(self, master, values,**kwargs):
        super().__init__(master, **kwargs)

        self.values = values




        


# Functions required to refresh the recommendation list
def show_tab(self, frame):
        for frm in self.btn_to_frame.values():
            frm.grid_remove()
        frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

def hide_tab(self, frame):
    frame.grid_remove()

# Functionality to open links
def callback(url):
    webbrowser.open_new(url)



app = App()
app.mainloop()