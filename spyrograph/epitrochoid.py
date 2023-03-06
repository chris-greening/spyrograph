import math
import turtle
from typing import Tuple, Union
import time

from ._roulette import _Roulette

class Epitrochoid(_Roulette):
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [self._calculate_x(theta) for theta in self.thetas]
        self.y = [self._calculate_y(theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def _trace_rolling_circle(
            self, small_circle_turtle: "turtle.Turtle", shape_turtle: "turtle.Turtle",
            x: Union[float, int], y: Union[float, int], theta: Union[float, int]
        ) -> None:
        """Trace the inner circle of the animation"""
        small_circle_turtle.clear()
        small_circle_turtle.seth(0)
        small_circle_turtle.up()

        # Draw red dot
        small_circle_turtle.goto(x, y)
        small_circle_turtle.dot(10, "red")

        # Draw circle
        small_circle_turtle.seth(0)
        small_circle_y=(self.R + self.r)*math.sin(theta) - self.r
        small_circle_x=(self.R + self.r)*math.cos(theta)
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

    def _calculate_x(self, theta: float) -> float:
        """Return calculated x-value from parametrized equation"""
        return (self.R + self.r)*math.cos(theta) - self.d*math.cos(((self.R+self.r)/self.r)*theta)

    def _calculate_y(self, theta: float) -> float:
        """Return calculated y-value from parametrized equation"""
        return (self.R + self.r)*math.sin(theta) - self.d*math.sin(((self.R+self.r)/self.r)*theta)