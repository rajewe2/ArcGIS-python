#fetch key information about ArcGIS Portal users

from arcgis import GIS
import pandas as pd
import keying

def establishConnection():
	#establish a connection to the ArcGIS Portal 
	#get pw from keyring
	pdub = keyring.get_password("GIS_portal","rajewe2")
	gis = GIS("myPortalUrl","rajewe2",pdub)

def searchUsers(gis):
	#search for a list of users
	users = gis.users.search('*') #,max_users=50
	return users

def listEmailAddrs(users):
	#parse user list and grab email addresss
	userEmailList = []
	for user in users:
		if str(user.email) != 'support@esri.com':
			userEmailList.append(user.email)

	#show email list that can be copied and pasted into email
	#due to string concatenation, ignore the las trecord initially; print after loop
	print(len(userEmailList))
	for aUser in userEmailList[:-1]:
		print(aUser + ';')
	print(userEmailList[-1])

def findNeverLogins(users):
	#Determine how many users have never logged in. Show count. List users.
	neverLoggedInCount = 0
	neverLoggedInList = []
	neverLoggedInAndPublisherCount = 0
	neverLoggedInAndPublisherList = []

	for user in users:
		if user.lastLogin == -1:
			neverLoggedInCount += 1
			neverLoggedInList.append(user.fullname)

		if user.lastLogin == -1 and user.role == 'org_publisher':
			neverLoggedInAndPublisherCount += 1
			neverLoggedInAndPublisherList.append(user.fullname)

	print("\n"+str(neverLoggedInCount) + " users have never logged into Portal: ")
	if neverLoggedInCount > 0:
		for name in neverLoggedInList:
			print("\t"+name)

	print("\n"+str(neverLoggedInAndPublisherCount) + " users are publishers that have never logged into Portal: ")
	if neverLoggedInAndPublisherCount > 0:
		for name in neverLoggedInAndPublisherList:
			print("\t"+name)

def userRoleBreakdown(users):
	#list user role and level status
	roles = {}
	levels = {}

	for user in users:
		try:
			if user.role in roles.keys():
				roles[user.role] += 1
			else:
				roles[user.role] = 1
			if user.level in level.keys():
				levels[user.level] += 1
			else:
				levels[user.level] = 1
		except:
			continue

	print("\nCurrent user role breakdown is as follows: ")
	for keys,vals in roles.items():
		print("\t"+keys,vals)


	print("\nCurrent user level breakdown is as follows: ")
	for keys,vals in levels.items():
		print("\t"+keys,vals)


gis = establishConnection() #create connection
users = searchUsers(gis) #search for users

findNeverLogins(users) #find users who never logged in
userRoleBreakdown(users) #summarize user roles
listEmailAddrs(users) #list user emails
	

	