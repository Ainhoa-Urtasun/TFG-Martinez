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
ilo2019 = ilo[ilo.time=='2019']
ilo2019 = ilo2019.fillna(0)

world = geopandas.read_file('/content/TFG-Martinez/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]

mydata = ilo2019.merge(world,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(20,20))
mydata.plot(column='Trade union density rate (%)',alpha=0.8,cmap='viridis',ax=ax,legend=True)
ax.set_title('Trade Union Density Rate in Percentages\n(source: International Labour Organization)')
ax.axis('off')
