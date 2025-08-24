from tkinter import*
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1899788ebc0cc85d713730e904329191").json()
    w_label1.config(text = data["weather"][0]["main"])
    wd_label1.config(text = data["weather"][0]["description"])
    temp_label1.config(text = str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text = data["main"]["pressure"])





win = Tk()

win.title("Weather Forcast")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win,text="Weather Forcast App",
                    font=("Time New Roman",30,"bold"))

name_label.place(x=25,y=50,height=50,width=450)


city_name = StringVar()
list_name =[
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

com = ttk.Combobox(win,text="Weather Forcast App",values = list_name,
                    font=("Time New Roman",20,"bold"),textvariable= city_name)

com.place(x=25,y=120,height=50,width=450)

# done_button = Button(win,text="Done",
#                     font=("Time New Roman",20,"bold"))
# done_button.place(y=190,height=50,width=100,x=200)

w_label = Label(win,text="Weather Climate",
                    font=("Time New Roman",16))
w_label.place(x=25,y=260,height=50,width=210)


w_label1 = Label(win,text="",
                    font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)




wd_label = Label(win,text="Weather Description",
                    font=("Time New Roman",17))
wd_label.place(x=25,y=330,height=50,width=210)

wd_label1 = Label(win,text="",
                    font=("Time New Roman",17))
wd_label1.place(x=250,y=330,height=50,width=210)


temp_label = Label(win,text="Temperature",
                    font=("Time New Roman",17))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",
                    font=("Time New Roman",17))
temp_label1.place(x=250,y=400,height=50,width=210)


pre_label = Label(win,text="pressure",
                    font=("Time New Roman",17))
pre_label.place(x=25,y=470,height=50,width=210)


pre_label1 = Label(win,text="",
                    font=("Time New Roman",17))
pre_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Done",
                    font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)





win.mainloop()