#fetch a feature layer in ArcGIS Portal as a DataFrame

from arcgis.gis import GIS
import pandas as pd

portalURL = ""
userName = ""
password = ""
myItemID = ""

#create a GIS connection
gis = GIS(portalURL,userName,password)

#fetch feature layer by portal itemID
item = gis.content.get(myItemID)
flayer = item.layers[0]

#read feature layer into dataFrame
myDF = flayer.query().df

myDF.head