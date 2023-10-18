import pandas
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pyproj
import warnings
warnings.filterwarnings("ignore")

ilo = pandas.read_csv('/content/TFG-Martinez/ILR_TIMT_NOC_RT_A-filtered-2023-10-18.csv')
print(ilo)

world = geopandas.read_file('/content/TFG-Martinez/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]
polygon = Polygon([(-25,35),(40,35),(40,75),(-25,75)])
europe = geopandas.clip(world,polygon)

mydata1 = mydata[mydata.time=='2022']
table = mydata.pivot(index='ADMIN',columns='time',values=['percentage']).reset_index()
table.columns = table.columns.droplevel(level=0)
table.rename(columns={'ADMIN':'GEO'},inplace=True)
table = table.rename_axis(columns=None)

mydata1 = mydata1.merge(europe,on='ADMIN',how='right')
mydata1 = geopandas.GeoDataFrame(mydata1,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(10,10))
mydata1.plot(column='percentage',alpha=0.8,cmap='cool',ax=ax,legend=True)
ax.set_title('Employed persons usually working from home from 20 to 64 years\nas a percentage of total employment (source: Eurostat)')
ax.axis('off')
