import turtle
import colorgram
import random
from turtle import Turtle,Screen
rgb_colors=[]
turtle.colormode(255)
timmy=turtle.Turtle()
"""colors = colorgram.extract('damien.jpg', 30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)"""

color_list=[(233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

for i in range(10):
    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)

timmy.setheading(90)
timmy.forward(50)
timmy.setheading(180)
timmy.forward(500)




