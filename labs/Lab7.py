## Line Plots
import matplotlib.pyplot as plt
import numpy as np

plt.plot(x, y,
         linewidth=2.0,             ## 2 pixels wide
         linestyle='--',            ## dashed line
         color='b',                 ## blue
         alpha=1.0,                 ## opaque
         marker='d')                ## thin diamond
=======================================================================================================================================================================
## Histograms
import numpy as np
import matplotlib.pyplot as plt

mu = 80
sigma = 7
x = np.random.normal(mu, sigma, size=200)

fig, ax = plt.subplots()

ax.hist(x, 20)
ax.set_title('Historgram')
ax.set_xlabel('bin range')
ax.set_ylabel('frequency')

fig.tight_layout()
plt.show()
=======================================================================================================================================================================

## 3D Surface Plots
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
X,Y = np.meshgrid(x,y)
Z = X*np.exp(-X2 - Y2)


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot a 3D surface

ax.plot_surface(X, Y, Z)

plt.show()
