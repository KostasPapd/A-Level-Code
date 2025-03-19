import requests
import datetime
import turtle
from PIL import Image


station = requests.get("http://api.open-notify.org/iss-now.json")
stationRes = station.json()
dateTimeObj = datetime.datetime.fromtimestamp(stationRes["timestamp"])

people = requests.get("http://api.open-notify.org/astros.json")
peopleRes = people.json()

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.setworldcoordinates(-180, -90, 180, 90)

image = Image.open('map.png')
image = image.resize((1920, 1080))
image = image.convert('RGB')
temp_file = "temp.gif"
image.save(temp_file, "GIF")

screen.register_shape('marker.gif')
iss = turtle.Turtle()
iss.shape('marker.gif')
iss.hideturtle()
iss.setheading(90)
iss.penup()
iss.goto(float(stationRes['iss_position']['longitude']), float(stationRes['iss_position']['latitude']))
iss.showturtle()

screen.bgpic(temp_file)

num_people = turtle.Turtle()
num_people.penup()
num_people.hideturtle()
num_people.color('black')
num_people.goto(-175, -25)
num_people.hideturtle()

num_people.write(f"Time of record: {dateTimeObj}\n"
                 f"People in space: {peopleRes['number']}\n"
                 f"Latitude: {stationRes['iss_position']['latitude']}\n"
                 f"Longitude: {stationRes['iss_position']['longitude']}\n")

screen.mainloop()
