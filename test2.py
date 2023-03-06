import numpy as np

from spyrograph import Hypotrochoid, Epitrochoid, Hypocycloid

# R = 573/2
# d = 600/2
# thetas = np.arange(0,365, .2)
# r = 791/2

R = 200
d = 50
thetas = np.arange(0,360,5)
r = 100
epitrochoid = Epitrochoid(R, r, d, thetas)
screen = epitrochoid.trace()

R = 300*1.12
d = 50*1.12
thetas = np.arange(0,360,2)
r = 150*1.12
hypotrochoid = Hypotrochoid(R, r, d, thetas)
screen = hypotrochoid.trace(screen = screen, color="red")

R = 50*1.45
d = 12.5*1.45
thetas = np.arange(0,360,5)
r = 25*1.45
epitrochoid = Hypocycloid(R, r, thetas)
epitrochoid.trace(exit_on_click=True, screen = screen, color = "blue")