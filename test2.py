import numpy as np

from spyrograph import Hypotrochoid

# R = 573/2
# d = 600/2
# thetas = np.arange(0,365, .2)
# r = 791/2

R = 600/1.2
d = 400/1.2
thetas = np.arange(0,365,2)
r = d

hypotrochoid = Hypotrochoid(R, r, d, thetas)
hypotrochoid.trace(exit_on_click=True, speed = 1, show_circles=True)

