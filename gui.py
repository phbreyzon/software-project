import customtkinter 
import webbrowser
from function import list_of_recommendations



        
# Main class initiation stuff
class App(customtkinter.CTk): 
    def __init__(self):
        super().__init__()
        
        # custom fonts 
        my_font = customtkinter.CTkFont(family="Roboto",size=14,weight="normal")

        # appareance mode
        customtkinter.set_appearance_mode("dark")
        

        # Layout of the main frame
        self.title("Music recommender")
        self.geometry("450x280")
        self.grid_columnconfigure(0, weight=1)
        self.scrollable_label_frame = Recommendations_list(master=self,title="recommendations", values=[""],url=[""],height=0,width=0)
                
        # Frame for the button and entry        
        self.primary_frame = customtkinter.CTkFrame(master=self, width=500, height=300, corner_radius=10)
        self.primary_frame.grid(row=1, column=0, padx=15, sticky="nswe", pady=(15,10))
        self.primary_frame.grid_columnconfigure(0,weight=1)
        
        ## The entry where you enter your songs
        self.entry = customtkinter.CTkEntry(master=self.primary_frame, placeholder_text="Enter song name")
        self.entry.grid(row=0, column=0, pady=(20,10), sticky="we", padx=65)
        
        ## Button for recommendations
        self.button = customtkinter.CTkButton(master=self.primary_frame, text="recommend", font=my_font,hover=True,command=lambda : button_action(self,self.scrollable_label_frame))
        self.button.grid(row=1, column=0, padx=65, pady=(20,10), sticky="we")
        
        ## The label for the description
        default_description_text="Enter your song in the textbox.\n set the number of recommendations with the slider"
        
        self.description_label = customtkinter.CTkLabel(master=self.primary_frame, text=default_description_text, width=10)
        self.description_label.grid(row=2, column=0, padx=25, sticky="we", pady=(8,15))



        # Frame for the description and slider
        self.slider_frame = customtkinter.CTkFrame(master=self, height=50,corner_radius=10)
        self.slider_frame.grid(row=2, column=0, padx=15, sticky="nswe", pady=(8,15))
        self.slider_frame.grid_columnconfigure(0,weight=1)
        

        ## slider for the number of recommendations 
        var = customtkinter.IntVar()

        self.slider = customtkinter.CTkSlider(self.slider_frame,width=30,from_=1,to=10, variable=var, number_of_steps=10)
        self.slider.grid(row=1, column=0, padx=25, sticky="we", pady=(8,15))
        self.slider.set(1)

        ## label to show how many recommendations are chosen 
        self.counter = customtkinter.CTkLabel(self.slider_frame, width=5,textvariable=var)
        self.counter.grid(row=1, column=1, padx=(0,20), sticky="we", pady=(8,15))



        # Button action when pressed
        def button_action(self, frame): 
            field_value = self.entry.get()
            number_of_recommendations = int(self.slider.get()) 

            ## when entry is empty
            if len(field_value) == 0:
                self.description_label.configure(text="warning: song is less than 1")
            
            else:
                self.description_label.configure(text=default_description_text)
                frame.destroy()
                
                array_2d= list_of_recommendations(field_value,number_of_recommendations)
                array_1d= [subarray[0] for subarray in array_2d]
                array_url= [subarray[1] for subarray in array_2d]

                frame.__init__(master=self, values=array_1d,title="recommendations",url=array_url,height=675, width=150) 
                frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=(30, 10))
                frame.grid_columnconfigure(0,weight=1)
                self.geometry("520x560")

  
        
# recommendation list frame
class Recommendations_list(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values,url,**kwargs):
        super().__init__(master, label_text=title)
        self.name_of_artists = values
        self.url = url
        
        for i,value in enumerate(self.name_of_artists):

            button = customtkinter.CTkButton(master=self,text=value,command=lambda url_text = url[i]: callback(url_text), anchor="w")
            button.grid(row=i, column=0, padx=20,pady=(10, 0), sticky="ew")            


# Opens the link given by the recommendation system
def callback(url):
    webbrowser.open(url)


# Declaring app and starting mainloop
app = App()
app.resizable(width=False, height=False)
app.mainloop()  