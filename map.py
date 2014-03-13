from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
#map.fillcontinents(color = 'gray')
map.bluemarble()
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
 
#x,y = map(lons, lats)
#map.plot(x, y, 'ro', markersize=6)
plt.title("Tweets Around the World")
plt.show()