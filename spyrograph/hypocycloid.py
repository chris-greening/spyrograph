from spyrograph.hypotrochoid import Hypotrochoid

class Hypocycloid(Hypotrochoid):
    def __init__(self, R, r, thetas) -> None:
        super().__init__(R, r, r, thetas)