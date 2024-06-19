import customtkinter 
import webbrowser
from function import list_of_recommendations


        
# Main class initiation stuff
class App(customtkinter.CTk): 
    def __init__(self):
        super().__init__()
        
        # custom fonts 
        my_font = customtkinter.CTkFont(family="Roboto",size=14,weight="normal")
        
        
        
        # experimenting with custom colour
        self.foreground_colour = "#181D23"
        self.button_colour ="#1C2833"
        
        
        
        # Layout of the main app
        self.title("Music recommender")
        self.geometry("480x230")
        self.grid_columnconfigure(0, weight=1)
        self.scrollable_label_frame = Recommendations_list(master=self,title="recommendations", values=[""],url=[""],height=0,width=0)
                
        # Frame for the button and entry        
        self.frame_for_button_and_entry = customtkinter.CTkFrame(master=self, width=500, height=300, corner_radius=10)
        self.frame_for_button_and_entry.grid(row=1, column=0, padx=15, sticky="nswe", pady=(15,10))
        self.frame_for_button_and_entry.grid_columnconfigure(0,weight=1)
        
        # The entry where you enter your songs
        self.entry = customtkinter.CTkEntry(master=self.frame_for_button_and_entry, placeholder_text="Enter recommendation")
        self.entry.grid(row=0, column=0, pady=(20,10), sticky="we", padx=65)
        
        
        # Button for recommendations
        self.button = customtkinter.CTkButton(master=self.frame_for_button_and_entry, text="recommend", font=my_font,hover=True,command=lambda : button_action(self,self.scrollable_label_frame))
        self.button.grid(row=1, column=0, padx=65, pady=20, sticky="we")
        
        
        # Button action when pressed
        def button_action(self, frame): 
            field_value = self.entry.get()
            
            if len(field_value) == 0:
                print("warning: song is less than 1")
            
            else:
                frame.destroy()
                
                array_2d= list_of_recommendations(field_value,10)
                array_1d = [subarray[0] for subarray in array_2d]
                array_url= [subarray[1] for subarray in array_2d]

                frame.__init__(master=self, values=array_1d,title="recommendations",url=array_url,height=550, width=150, fg_color=self.foreground_colour) 
                frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=(30, 10))
                frame.grid_columnconfigure(0,weight=1)
                self.geometry("520x560")
             
        
        # Frame for the description
        self.description_frame = customtkinter.CTkFrame(master=self, height=50,corner_radius=10)
        self.description_frame.grid(row=2, column=0, padx=15, sticky="nswe", pady=(8,15))
        self.description_frame.grid_columnconfigure(0,weight=1)
        
        self.label = customtkinter.CTkLabel(master=self.description_frame, text="Enter the sond you want to get recommendations for in the text field")
        self.label.grid(row=0, column=0, padx=25, sticky="we", pady=(8,15))



        
        
        
# Definition of the recommendation list
class Recommendations_list(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values,url,**kwargs):
        super().__init__(master, label_text=title)
        self.name_of_artists = values
        self.url = url
        
        for i,value in enumerate(self.name_of_artists):

            button = customtkinter.CTkButton(master=self,text=value,command=lambda url_text = url[i]: callback(url_text), anchor="w", fg_color="#515A5A")
            button.grid(row=i, column=0, padx=20,pady=(10, 0), sticky="ew")
            
        
    
def callback(url):
    webbrowser.open(url)



app = App()
app.resizable(width=False, height=False)
app.mainloop()  