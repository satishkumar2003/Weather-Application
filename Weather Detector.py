import requests
import urllib.request
API = "fe91480ac0c6713160d8786a95188909"
city = input("Enter name of city:")
URL = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API
data = requests.get(URL)


def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=2)
        return True
    except:
        return False

x = internet_on()
if x == True:
    if data.status_code == 200:
            res = data.json( )
            print("res")
            """main = res['main']
            temp= main['temp']
            feel = main['feels_like']
            mn = main['temp_min']
            mx =main['temp_max']
            print(f'Temperature: {temp}')
            print(f'Feels like: {feel}')
            print(f'Minimum Temperature: {mn}')
            print(f'Maximum Temperature: {mx}')"""
    else:
        print("Error occured")
    



