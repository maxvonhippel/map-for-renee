# libraries
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# Initialize
m=Basemap(llcrnrlon=-172, llcrnrlat=62.7, # corner 1
          urcrnrlon=-167.75, urcrnrlat=64, # corner 2
          resolution='h',
          projection='mill')

# Continent in grey (change colors using hex codes if you want them to differ)
m.fillcontinents(color='#808080', lake_color='#d3d3d3')
# m.etopo(scale=3) # If you want color / topography, try this and comment out above line. 
# In that case you may need to change the scale to increase resolution.  Just screw around
# with it and see what works.
m.drawcountries()
m.drawrivers()

# Add Latitude and Longitude Lines
lat_start = 62.7 
lat_end = 64 
lat_spacing = 0.2

lon_start = -172
lon_end = -167.75
lon_spacing = 1

parallels = np.arange(lat_start, lat_end, lat_spacing) # Define the latitude range and interval
meridians = np.arange(lon_start, lon_end, lon_spacing) # Define the longitude range and interval
m.drawparallels(parallels, labels=[1,0,0,0], fontsize=10, linewidth=0.1) # Draw parallels (latitude lines). The labels list controls where the labels will be drawn
m.drawmeridians(meridians, labels=[0,0,0,1], fontsize=10, linewidth=0.1) # Draw meridians (longitude lines). The labels list controls where the labels will be drawn



# Show the coast lines in black
m.drawcoastlines(color='black', linewidth=1)

locations = [
    {
        "coordinates": (-171.7411, 63.7797),
        "label_coordinates": (-171.7411 + 0.08, 63.7797 + 0.08),
        "label": "Gambell",
    },
    {
        "coordinates": (-170.4789, 63.6942),
        "label_coordinates": (-170.4789 + 0.08, 63.6942 + 0.08),
        "label": "Savoonga",
    },
    {
        "coordinates": (-168.6922, 63.2950),
        "label_coordinates": (-168.6922 + 0.05, 63.2950),
        "label": "Northeast\nCape",
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

