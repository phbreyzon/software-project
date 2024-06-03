import customtkinter
from CTkListbox import *
import webbrowser
from recommendation import recommend_songs_by_cluster, DEFAULT_FEATURE_COLS


# Main class initiation stuff
class App(customtkinter.CTk): 
    def __init__(self):
        super().__init__()

        # Layout of the main app
        self.title("Music recommender")
        self.geometry("860x520")
        self.grid_columnconfigure(0, weight=1)
        self.scrollable_checkbox_frame = ScrollableList(master=self, width=300, height=200, corner_radius=10)
        self.scrollable_checkbox_frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=(30, 10))







# Definition of the recommendation list
class ScrollableList(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text="new text")
        self.label.grid(row=0, column=0, padx=20)




        


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