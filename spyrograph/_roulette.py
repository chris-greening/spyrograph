import math
import turtle
from typing import Tuple, Union
import time
from abc import ABC, abstractmethod

class _Roulette(ABC):
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [self._calculate_x(theta) for theta in self.thetas]
        self.y = [self._calculate_y(theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def trace(self, screen_size: Tuple[int, int] = (1000, 1000), exit_on_click: bool = False, color: str = "black", hide_turtle: bool = True, show_circles: bool = False, frame_pause: float = 0, screen: "turtle.Screen" = None) -> "turtle.Screen":
        """Trace the roulette shape using turtle

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

        Returns
        -------
        screen: turtle.Screen
            Screen that the turtle is drawn on
        """
        if screen is None:
            screen = turtle.Screen()
            screen.setup(*screen_size)
        turtle.tracer(False)

        shape_turtle = turtle.Turtle()
        rolling_circle_turtle = turtle.Turtle()
        fixed_circle_turtle = turtle.Turtle()
        rolling_circle_turtle.hideturtle()
        fixed_circle_turtle.hideturtle()
        if hide_turtle:
            shape_turtle.hideturtle()
        if show_circles:
            self._trace_fixed_circle(fixed_circle_turtle)
        
        first = True 
        shape_turtle.up()
        shape_turtle.color(color)
        for x, y, theta in self.coords:
            shape_turtle.goto(x, y)
            if show_circles:
                self._trace_outer_circle(rolling_circle_turtle, shape_turtle, x, y, theta)
            if first:
                first = False
                shape_turtle.down()
            turtle.update()
            time.sleep(frame_pause)
        if exit_on_click:
            turtle.exitonclick()
        return screen

    def _trace_fixed_circle(self, fixed_circle_turtle: "turtle.Turtle") -> None:
        """Trace the outer circle of the animation"""
        fixed_circle_turtle.up()
        fixed_circle_turtle.seth(0)
        fixed_circle_turtle.goto(0,-self.R)
        fixed_circle_turtle.down()
        fixed_circle_turtle.circle(self.R,steps=200)

    def _trace_rolling_circle(
            self, rolling_circle_turtle: "turtle.Turtle", shape_turtle: "turtle.Turtle",
            x: Union[float, int], y: Union[float, int], theta: Union[float, int]
        ) -> None:
        """Trace the inner circle of the animation"""
        self._rolling_circle_init(rolling_circle_turtle)
        self._draw_trace_dot(rolling_circle_turtle, x, y)
        self._draw_rolling_circle_dot(rolling_circle_turtle, theta)
        rolling_circle_x, rolling_circle_y = self._draw_rolling_circle_focus()
        self._draw_rolling_circle_focus(rolling_circle_turtle, rolling_circle_x, rolling_circle_y)
        self._connect_focus_to_trace_dots(rolling_circle_turtle, shape_turtle)

    def _connect_focus_to_trace_dots(self, rolling_circle_turtle: "turtle.Turtle", shape_turtle: "turtle.Turtle") -> None:
        """Draw line from focus to the trace that's drawing the shape"""
        rolling_circle_turtle.down()
        rolling_circle_turtle.seth(rolling_circle_turtle.towards(shape_turtle))
        rolling_circle_turtle.fd(self.d)

    def _draw_rolling_circle_focus_dot(self, rolling_circle_turtle: "turtle.Turtle", rolling_circle_x: Union[float, int], rolling_circle_y: Union[float, int]) -> None:
        """Draw the center of the rolling circle"""
        rolling_circle_turtle.up()
        rolling_circle_turtle.goto(rolling_circle_x, rolling_circle_y + self.r)
        rolling_circle_turtle.dot(10, "blue")

    def _draw_rolling_circle(self, rolling_circle_turtle: "turtle.Turtle", theta) -> None:
        """Draw the rolling circle on the screen"""
        rolling_circle_turtle.seth(0)
        rolling_circle_y=self._circle_offset()*math.sin(theta) - self.r
        rolling_circle_x=self._circle_offset()*math.cos(theta)
        rolling_circle_turtle.goto(rolling_circle_x, rolling_circle_y)
        rolling_circle_turtle.down()
        rolling_circle_turtle.color("black")
        rolling_circle_turtle.circle(self.r,steps=200)
        return rolling_circle_x, rolling_circle_y

    def _draw_trace_dot(self, rolling_circle_turtle: "turtle.Turtle", x: Union[int, float], y: Union[int, float]) -> None:
        """Draw rolling circle outer trace"""
        rolling_circle_turtle.goto(x, y)
        rolling_circle_turtle.dot(10, "red")

    def _rolling_circle_init(self, rolling_circle_turtle: "turtle.Turtle") -> None:
        """Set iteration's initial conditions for rolling circle"""
        rolling_circle_turtle.clear()
        rolling_circle_turtle.seth(0)
        rolling_circle_turtle.up()

    @abstractmethod
    def _circle_offset(self) -> float:
        """Return rolling circle offset from fixed circle"""
        return self.R + self.r

    @abstractmethod
    def _calculate_x(self, theta: float) -> float:
        """Return calculated x-value from parametrized equation"""

    @abstractmethod
    def _calculate_y(self, theta: float) -> float:
        """Return calculated y-value from parametrized equation"""
