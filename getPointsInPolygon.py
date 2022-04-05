#fetch the points in an existing polygon featureclass and create a new point featureclass from those points

import arcpy

#define workspace and key parameters
arcpy.env.workspace = r'\\'
inputPolygonFeatureClass = "USAStateBoudaries_SimplifyP"
templateFeatureClass = "myPoints"
outputPointFeatureClass = "myPoints4"

#lookup feature classes if needed. Could do more here
myPolygonFeatureClasses = arcpy.ListFeatureClasses('*',"POLYGON")
print(myPolygonFeatureClasses)

#check for output feature class existence. If it exists, delete data. If not, create feature class
if(arcpy.Exists(outputPointFeatureClass)):
    print("Delete existing data")
    arcpy.management.DeleteFeatures(outputPointFeatureClass)
else:
    print("Create feature class")
    arcpy.management.CreateFeatureclass(out_path = arcpy.env.workspace,
                                        out_name = outputPointFeatureClass,
                                        geometry_type = "POINT",
                                        template = templateFeatureClass)
                                        
#establish search cursor for featureclass containing desired geometry
polygonSearchCursor = arcpy.da.SearchCursor(inputPolygonFeatureClass,"Shape@")

#geometry holder
pointsInPolygon = []

#loop through rows of search cursor for polygon
#receive transaction error when trying to insert at the same time in the same workspace
#so moved inserting to next block from list
for polyObject in polygonSearchCursor:
    for arrayObject in polyObject[0]:
        for x, row in enumerate(arrayObject):
            pointsInPolygon.append((row.X,row.Y))
            
del polygonSearchCursor

#add points to the new featureclass; establish insert cursor for updating data
pointCursor = arcpy.da.InsertCursor(outputPointFeatureClass,["labelValue","SHAPE@XY"])

for x, myPoints in enumerate(pointsInPolygon):
    xy = [x+1,myPoints]
    pointCursor.insertRow(xy)
    
del pointCursor

#establish search cursor for results table
resultRows = arcpy.da.SearchCursor(outputPointFeatureClass,["labelValue","SHAPE@XY"])

#loop through rows of cursor and print output rows
for aRow in resultRows:
    print(aRow)
    
del resultRows
        
        
        
        