import math

from ._roulette import _Roulette

class Hypotrochoid(_Roulette):
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [self._calculate_x(theta) for theta in self.thetas]
        self.y = [self._calculate_y(theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def _circle_offset(self) -> float:
        """Return rolling circle offset from fixed circle"""
        return self.R - self.r

    def _calculate_x(self, theta: float) -> float:
        """Return calculated x-value from parametrized equation"""
        return self._circle_offset()*math.cos(theta) + self.d*math.cos((self._circle_offset()/self.r)*theta)

    def _calculate_y(self, theta: float) -> float:
        """Return calculated y-value from parametrized equation"""
        return self._circle_offset()*math.sin(theta) + self.d*math.sin((self._circle_offset()/self.r)*theta)
