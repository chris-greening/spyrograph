import numpy as np

from spyrograph import Hypotrochoid, Epitrochoid

# R = 573/2
# d = 600/2
# thetas = np.arange(0,365, .2)
# r = 791/2

R = 300
d = 50
thetas = np.arange(0,7,.05)
r = 100

# hypotrochoid = Hypotrochoid(R, r, d, thetas)
# hypotrochoid.trace(exit_on_click=True)

epitrochoid = Epitrochoid(R, r, d, thetas)
epitrochoid.trace(exit_on_click=True, show_circles=True)