import pandas
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pyproj
import warnings
warnings.filterwarnings("ignore")

lp = pandas.read_csv('/content/TFG-Martinez/GDP_211P_NOC_NB_A-full-2023-10-18.csv')
leadernet = lp[lp['ref_area.label'].isin(['Spain','Mexico','Brazil','Uruguay','United States','India','South Africa'])]

lp = lp[['ref_area.label','time','obs_value']]
lp.rename(columns={'ref_area.label':'ADMIN','obs_value':'LP'},inplace=True)
lp1 = lp[['ADMIN','LP']]
lp1 = lp1.groupby(['ADMIN']).mean().reset_index()
lp1 = lp1.fillna(0)

world = geopandas.read_file('/content/TFG-Martinez/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]
world.loc[world.ADMIN=='United States of America','ADMIN'] = 'United States'

mydata = lp1.merge(world,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')

fig,ax = plt.subplots(1,figsize=(25,25))
mydata.plot(column='LP',alpha=0.8,cmap='viridis',ax=ax,legend=True,legend_kwds={'shrink':0.3})
ax.set_title('Output per worker (GDP constant 2017 international $ at PPP)\nSource: International Labour Organization',size='x-large')
ax.axis('off')
fig.savefig('/content/TFG-Martinez/World.png')
