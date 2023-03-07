from spyrograph.epitrochoid import Epitrochoid

class Epicycloid(Epitrochoid):
    def __init__(self, R, r, thetas) -> None:
        super().__init__(R, r, r, thetas)