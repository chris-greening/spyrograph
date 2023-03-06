import numpy as np

from spyrograph import Hypotrochoid

# Initial conditions
R = 100
d = 400/1.2
thetas = np.arange(0,360,1)
r = d

# Draw the hypotrochoid
hypotrochoid = Hypotrochoid(R, r, d, thetas)
hypotrochoid.trace()

