import requests
import tkinter as tk


def get_weather(city):
    API="fe91480ac0c6713160d8786a95188909"
    URL= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid="+API
    try:
        data = requests.get(URL)
        if data.status_code == 200:
            res = data.json( )
            main = res['main']
            temp= main['temp']
            desc = res['weather'][0]['description']
            mn = main['temp_min']
            mx =main['temp_max']
            
            result = 'Temperature: %s Celsius\n Description: %s\n Minimum Temperature: %s Celsius\n Maximum Temperature: %s Celsius\n' % (temp,desc,mn,mx)
            
            label['text'] = result
            
        else:
            label['text'] = 'Error Occured'
    except:
        label['text'] = 'Please check your internet connection'



_height,_width = 385,626
root = tk.Tk()
root.title('Weather App')


canvas = tk.Canvas(root,height = _height,width = _width)
canvas.pack()

frame = tk.Frame(root,bg='#afede2',bd=5)
frame.place(relheight=1,relwidth=1)

background_image = tk.PhotoImage(file= "sky.png")
background_label = tk.Label(frame, image=background_image)
background_label.place(relwidth=1, relheight=1)

city_entry = tk.Label(frame,bg = '#80c1ff',text="Enter name of city ",font=('MS Serif',16),bd=5)
city_entry.place(relx=0.05,rely=0.2,relheight=0.1,relwidth=0.3)

weather_button=tk.Button(frame,text='Get Weather',font=('MS Serif',16),command= lambda:get_weather(entry_box.get()))
weather_button.place(relx=0.5,rely=0.32,relwidth=0.3,relheight=0.1,anchor='n')

entry_box = tk.Entry(frame,font=('Arial',16))
entry_box.place(relx=0.36,rely=0.2,relwidth=0.6, relheight=0.1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.45, relwidth=0.90,relheight=0.48,anchor='n')

label = tk.Label(lower_frame,justify='left',wraplength=360,font=('MS Serif',18))
label.place(relwidth=1, relheight=1)

root.mainloop()
