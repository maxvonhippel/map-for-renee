# libraries
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# Initialize
m=Basemap(llcrnrlon=-172, llcrnrlat=62.7,
	      urcrnrlon=-167.75, urcrnrlat=64,
	      resolution='h',
	      projection='mill')

# Continent in green
m.fillcontinents(color='#808080',lake_color='#d3d3d3')

m.drawcountries()

m.drawrivers()

# Show the coast lines in black
m.drawcoastlines(color='black', linewidth=1)

# North east cape = 63.2950° N, 168.6922° W
# Gambell         = 63.7797° N, 171.7411° W
# Savoonga        = 63.6942° N, 170.4789° W

x_nec, y_nec = m(-168.6922, 63.2950) 
nec = m.plot(x_nec, y_nec, 'wo')
plt.setp(nec, 'markersize', 4., 'markeredgecolor', 'black')

x_nec_label, _ = m(-168.6922 + 0.05, 63.2950)

plt.text(x_nec_label, y_nec, 
		 "Northeast\nCape",
	     fontsize=12,
	     fontweight='bold', 
	     ha='left',
	     va='top',
	     color='k')

x_gam, y_gam = m(-171.7411, 63.7797) 
gam = m.plot(x_gam, y_gam, 'wo')
plt.setp(gam, 'markersize', 4., 'markeredgecolor', 'black')

plt.text(x_gam, y_gam + 1.3, 
		 'Gambell',
	     fontsize=12,
	     fontweight='bold', 
	     ha='left',
	     va='bottom',
	     color='k')

x_sav, y_sav = m(-170.4789, 63.6942) 
sav = m.plot(x_sav, y_sav, 'wo')
plt.setp(sav, 'markersize', 4., 'markeredgecolor', 'black')

plt.text(x_sav, y_sav + 1.3, 
		 'Savoonga',
	     fontsize=12,
	     fontweight='bold', 
	     ha='left',
	     va='bottom',
	     color='k')



 
plt.savefig('renee.png', dpi=500)

