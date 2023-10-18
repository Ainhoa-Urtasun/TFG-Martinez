import pandas
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pyproj
import warnings
warnings.filterwarnings("ignore")

ilo = pandas.read_csv('/content/TFG-Martinez/ILR_TUMT_NOC_RT_A-filtered-2023-10-18.csv')

ilo = ilo[['ref_area.label','time','obs_value']]
ilo.rename(columns={'ref_area.label':'ADMIN','obs_value':'Trade union density rate (%)'},inplace=True)
ilo1 = ilo[['ADMIN','Trade union density rate (%)']]
ilo1 = ilo1.groupby(['ADMIN']).mean().reset_index()
ilo1 = ilo1.fillna(0)

world = geopandas.read_file('/content/TFG-Martinez/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]

mydata = ilo1.merge(world,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(50,50))
mydata.plot(column='Trade union density rate (%)',alpha=0.8,cmap='viridis',ax=ax,legend=True,legend_kwds={'shrink':0.3})
ax.set_title('Trade Union Density Rate (%)\nSource: International Labour Organization')
ax.axis('off')
fig.savefig('/content/TFG-Martinez/World.png')
