import customtkinter
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
        self.scrollable_label_frame = Recommendations_list(master=self,title="recommendations", values=[""],url=[""])
                
        self.frame_for_button_and_entry = customtkinter.CTkFrame(master=self, width=300, height=200, corner_radius=10,)
        self.frame_for_button_and_entry.grid(row=1, column=0, sticky="nsew", padx=30, pady=(30, 10))
        
        
        self.entry = customtkinter.CTkEntry(master=self.frame_for_button_and_entry, placeholder_text="Enter recommendation")
        self.entry.grid(row=0, column=0, padx=20, pady=20)
        
    
        
        self.button = customtkinter.CTkButton(master=self.frame_for_button_and_entry, text="recommend",command=lambda : button_action(self,self.scrollable_label_frame))
        self.button.grid(row=1, column=1, padx=20, pady=20)
        
        
        
        def button_action(self, frame): 
            frame.destroy()
            
            
            array_2d= list_of_recommendations(self.entry.cget("state"),5)
             
            array_1d = [subarray[0] for subarray in array_2d]
            
            array_url= [subarray[1] for subarray in array_2d]

            frame.__init__(master=self, values=array_1d,title="recommend",url=array_url) 
            frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=(30, 10))
            
        
        











# Definition of the recommendation list
class Recommendations_list(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values,url):
        super().__init__(master, label_text=title)
        self.name_of_artists = values
        
        for i,value in enumerate(self.name_of_artists):
            label = customtkinter.CTkButton(master=self,text=value, command= callback(url[i]))
            label.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            
        
    





# Functionality to open links
def callback(url):
    webbrowser.open_new(url)



app = App()
app.mainloop()