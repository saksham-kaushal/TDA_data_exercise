# import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

x = [i for i in range(3,21)]
x.append(25)

y = [342.527,710.071,794.189,
852.760,847.537,759.236, 657.519, 564.448, 
503.706, 452.286, 422.322, 412.725, 388.763, 
367.845, 354.948, 336.155, 318.092, 303.514, 236.883]

sns.set()
plt.plot(x,y)
plt.xlabel('Aperture (width of semi-major axis) in pixels')
plt.ylabel('Signal to noise ratio')
plt.savefig('./plots/optimal_aperture_phot_00.png', resolution=480)