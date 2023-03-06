import numpy as np

from spyrograph import Hypotrochoid, Epitrochoid, Hypocycloid, Epicycloid, Deltoid

# R = 573/2
# d = 600/2
# thetas = np.arange(0,365, .2)
# r = 791/2

R = 100
d = 400/1.2
thetas = np.arange(0,30,1)
r = d

deltoid = Deltoid(R, thetas)
deltoid.trace(exit_on_click=True, show_circles=True)