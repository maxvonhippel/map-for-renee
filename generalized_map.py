# libraries
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# Initialize
m=Basemap(llcrnrlon=-172, llcrnrlat=62.7, # corner 1
          urcrnrlon=-167.75, urcrnrlat=64, # corner 2
          resolution='h',
          projection='mill')

# Continent in green
m.fillcontinents(color='#808080', lake_color='#d3d3d3')
m.drawcountries()
m.drawrivers()

# Show the coast lines in black
m.drawcoastlines(color='black', linewidth=1)

locations = [
    {
        "coordinates": (-168.6922, 63.2950),
        "label_coordinates": (-168.6922 + 0.05, 63.2950),
        "label": "Northeast\nCape",
    },
    {
        "coordinates": (-171.7411, 63.7797),
        "label_coordinates": (-171.7411, 63.7797 + 1.3),
        "label": "Gambell",
    },
    {
        "coordinates": (-170.4789, 63.6942),
        "label_coordinates": (-170.4789, 63.6942 + 1.3),
        "label": "Savoonga",
    },
]

for entry in locations:
    
    coordinates = entry["coordinates"]
    (lat, lon) = coordinates
    label_coordinates = entry["label_coordinates"]
    (lab_lat, lab_lon) = label_coordinates
    label = entry["label"]

    x, y = m(lat, lon)
    nec = m.plot(x, y, 'wo')
    plt.setp(nec, 'markersize', 4., 'markeredgecolor', 'black')

    x_lab, y_lab = m(lab_lat, lab_lon)
    plt.text(x_lab, y_lab, label, 
        fontsize=12,
         fontweight='bold', 
         ha='left',
         va='top',
         color='k')

 
plt.savefig('map.png', dpi=500)

