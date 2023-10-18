import pandas
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pyproj
import warnings
warnings.filterwarnings("ignore")

ilo = pandas.read_csv('/content/TFG-Martinez/ILR_TUMT_NOC_RT_A-filtered-2023-10-18.csv')
print(ilo)

ilo = ilo[['ref_area.label','time','obs_value']]
ilo.rename(columns={'ref_area.label':'ADMIN','Trade union density rate (%)'},inplace=True)
table = table.rename_axis(columns=None)

world = geopandas.read_file('/content/TFG-Martinez/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]

mydata = ilo.merge(world,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(10,10))
mydata.plot(column='percentage',alpha=0.8,cmap='cool',ax=ax,legend=True)
ax.set_title('Employed persons usually working from home from 20 to 64 years\nas a percentage of total employment (source: Eurostat)')
ax.axis('off')
