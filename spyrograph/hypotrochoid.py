import math
import turtle
from typing import Tuple
import time

class Hypotrochoid:
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [calculate_x(R, r, d, theta) for theta in self.thetas]
        self.y = [calculate_y(R, r, d, theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def trace(self, speed: int = 0, screen_size: Tuple[int, int] = (1000, 1000), exit_on_click: bool = False, color: str = "black", hide_turtle: bool = True, show_circles: bool = False) -> None:
        """Turtle draw the hypotrochoid"""
        screen = turtle.Screen()
        screen.setup(*screen_size)
        turtle.tracer(False)

        shape_turtle = turtle.Turtle()
        small_circle_turtle = turtle.Turtle()
        large_circle_turtle = turtle.Turtle()
        small_circle_turtle.hideturtle()
        large_circle_turtle.hideturtle()
        if hide_turtle:
            shape_turtle.hideturtle()

        if show_circles:
            large_circle_turtle.up()
            large_circle_turtle.seth(0)
            large_circle_turtle.goto(0,-self.R)
            large_circle_turtle.down()
            large_circle_turtle.circle(self.R,steps=200)
        
        first = True 
        shape_turtle.up()
        for x, y, theta in self.coords:
            shape_turtle.goto(x, y)

            # Draw small circle
            if show_circles:
                # Reset 
                small_circle_turtle.clear()
                small_circle_turtle.seth(0)
                small_circle_turtle.up()

                # Draw red dot 
                small_circle_turtle.goto(x, y)
                small_circle_turtle.dot(10, "red")

                # Draw circle
                small_circle_turtle.seth(0)
                small_circle_y=(self.R - self.r)*math.sin(theta) - self.r
                small_circle_x=(self.R - self.r)*math.cos(theta)
                small_circle_turtle.goto(small_circle_x, small_circle_y)
                small_circle_turtle.down()
                small_circle_turtle.color("black")
                small_circle_turtle.circle(self.r,steps=200)

                # Draw center blue dot
                small_circle_turtle.up()
                small_circle_turtle.goto(small_circle_x, small_circle_y + self.r)
                small_circle_turtle.dot(10, "blue")

                #Draw line
                small_circle_turtle.down()
                small_circle_turtle.seth(small_circle_turtle.towards(shape_turtle))
                small_circle_turtle.fd(self.d)
            if first:
                first = False
                shape_turtle.down()
            turtle.update()
        if exit_on_click:
            turtle.exitonclick()

def calculate_x(R: float, r: float, d: float, theta: float) -> float:
    """Return calculated x-value from parametrized equation"""
    return (R - r)*math.cos(theta) + d*math.cos(((R-r)/r)*theta)

def calculate_y(R: float, r: float, d: float, theta: float) -> float:
    """Return calculated y-value from parametrized equation"""
    return (R - r)*math.sin(theta) + d*math.sin(((R-r)/r)*theta)
