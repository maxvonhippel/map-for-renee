# libraries
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# Initialize
m=Basemap(llcrnrlon=-180, llcrnrlat=60,urcrnrlon=-160,urcrnrlat=75,resolution='h')

# Background color:
# m.drawmapboundary(fill_color='#A6CAE0')

# Continent in green
m.fillcontinents(color='#69b2a2',lake_color='#A6CAE0')

m.drawcoastlines()
m.drawcountries()
m.etopo()
m.drawrivers()

# Show the coast lines in black
m.drawcoastlines(color='black', linewidth=2)
 
plt.show()
