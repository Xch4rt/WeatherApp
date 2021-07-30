import tkinter as tk
import requests
import time

canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('Weather App')
f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')

def getWeather(canvas):
	API_Key = 'bc1d9580667be7bb90d5b2f5c0f7c9c4'
	city = txtField.get()

	base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

	weather_data = requests.get(base_url).json()
	condition = weather_data['weather'][0]['main']
	temp = int(weather_data['main']['temp'] - 273.15)
	min_temp = int(weather_data['main']['temp_min'] - 273.15)
	max_temp = int(weather_data['main']['temp_max'] - 273.15)

	pressure = weather_data['main']['pressure']
	humidity = weather_data['main']['humidity']

	wind = weather_data['wind']['speed']

	sunrise = time.strftime('%I:%M:%S', time.gmtime(weather_data['sys']['sunrise'] - 21600))
	sunset = time.strftime('%I:%M:%S', time.gmtime(weather_data['sys']['sunset'] - 21600))

	info = condition + '\n' + str(temp) + '°C'
	data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
	label1.config(text = info)
	label2.config(text = data)

txtField = tk.Entry(canvas, justify='center', width = 20, font = t)
txtField.pack(pady=20)
txtField.focus()
txtField.bind('<Return>', getWeather)

label1 =tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
