#determine the groups for an ArcGIS Portal user

from arcgis.gis import GIS
import keyring

portalURL = ""
portalUserName = ""

#create a GIS connection
gis = GIS(portalURL,portalUserName,keyring.get_password("GIS_portal_user","rajewe2"))

#search for user of interest
myUser = gis.users.search(userOfInterest, max_users=1)

#output
print("%s is part of %s groups." % (myUser, len(myUser[0].groups)))
print(myUser[0].groups)

for group in myUser[0].groups:
	print(group.title)