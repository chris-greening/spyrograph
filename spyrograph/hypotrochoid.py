import math
import turtle
from typing import Tuple, Union
import time

class Hypotrochoid:
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [self._calculate_x(theta) for theta in self.thetas]
        self.y = [self._calculate_y(theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def trace(self, screen_size: Tuple[int, int] = (1000, 1000), exit_on_click: bool = False, color: str = "black", hide_turtle: bool = True, show_circles: bool = False, frame_pause: float = 0) -> None:
        """Trace the hypotrochoid using turtle

        Parameters
        ----------
        screen_size: Tuple[int, int]
            Length and width of the output screen
        exit_on_click: bool = False
            Pause the final animation until the user clicks to exit the window
        color: str = "black"
            Color of the primary tracing
        hide_turtle: bool = True
            Hide the turtle icon while tracing
        show_circles: bool = False
            Show the inner and outer circles that compose the trace
        frame_pause: float = 0
            Time in seconds to pause each individual frame for
        """
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
            self._trace_outer_circle(large_circle_turtle)
        
        first = True 
        shape_turtle.up()
        shape_turtle.color(color)
        for x, y, theta in self.coords:
            shape_turtle.goto(x, y)
            if show_circles:
                self._trace_inner_circle(small_circle_turtle, shape_turtle, x, y, theta)
            if first:
                first = False
                shape_turtle.down()
            turtle.update()
            time.sleep(frame_pause)
        if exit_on_click:
            turtle.exitonclick()

    def _trace_outer_circle(self, large_circle_turtle: "turtle.Turtle") -> None:
        """Trace the outer circle of the animation"""
        large_circle_turtle.up()
        large_circle_turtle.seth(0)
        large_circle_turtle.goto(0,-self.R)
        large_circle_turtle.down()
        large_circle_turtle.circle(self.R,steps=200)

    def _trace_inner_circle(
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

    def _calculate_x(self, theta: float) -> float:
        """Return calculated x-value from parametrized equation"""
        return (self.R - self.r)*math.cos(theta) + self.d*math.cos(((self.R-self.r)/self.r)*theta)

    def _calculate_y(self, theta: float) -> float:
        """Return calculated y-value from parametrized equation"""
        return (self.R - self.r)*math.sin(theta) + self.d*math.sin(((self.R-self.r)/self.r)*theta)
