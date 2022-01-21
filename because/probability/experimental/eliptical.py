import matplotlib.pyplot as plt
import numpy as np
import math
import scipy
from scipy import special


def normalQ(mu, sigma, p):
    q = mu + sigma * 2**.5 * special.erfinv(2*p - 1)
    return q

math.erf


lims = (-5,5)

fig = plt.figure(figsize=(200,150))
ax = fig.add_subplot(projection='3d')
ax.axes.set_xlim3d(lims)
ax.axes.set_ylim3d(lims)
ax.axes.set_zlim3d(lims)
#ax.set_axis_off()
# Make data

numElipses = 3
alpha = .16 / numElipses
color = (0,0,1)
def plotNormal(mu, sigma):

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    ringwidth = normalQ(0,1, .55) - normalQ(0,1,.45)

    x = sigma[0] * np.outer(np.cos(u), np.sin(v)) * ringwidth
    y = sigma[1] * np.outer(np.sin(u), np.sin(v)) * ringwidth
    z = sigma[2] * np.outer(np.ones(np.size(u)), np.cos(v)) * ringwidth
    plt.autoscale(False)

    # Plot the surfaces
    for i in range(10):
        j = i + 2
        print('ringwidth = ', ringwidth)
        xt = x + mu[0]
        yt = y + mu[1]
        zt = z + mu[2]
        if True:
            ax.plot_surface(xt, yt, zt, color = color, alpha = alpha)
        if j < 10:
            newringwidth = normalQ(0, 1, .5+j*.05) - \
                normalQ(0,1, .5 - j*.05)
        else:
            newringwidth = normalQ(0,1,.995) - normalQ(0,1,.005)
        increase = newringwidth / ringwidth
        print('increase = ', increase)
        ringwidth = newringwidth
        #increase = abs(np.random.normal(0, .3)) + 1
        #increase = np.random.normal(1.5, .005, x.shape[0])
        x = x * increase
        #increase = np.random.normal(1.5, .005, y.shape[0])
        #increase = abs(np.random.normal(0, .3)) + 1
        y = y * increase
        #increase = abs(np.random.normal(0, .3)) + 1
        #increase = np.random.normal(1.5, .005, x.shape[0])
        z = z * increase

    #ax.plot_surface(x, y, z, color = (0,0,1.0), alpha = alpha)
plotNormal((0,0,0), (1, .7, .5))
plotNormal((.5,.2,-.2), (1, .6, .6))
plotNormal((-2.4,-2.2,-2.2), (1, .7, .6))
plt.show()
