import sys
import datetime

def makeUser(info):
	index = 0
   user = User()
  	user.emplID = info[index]
	user.firstName = info[++index]
	user.lastName = info[++index]
	user.email = info[++index] #also used as username
	user.password = info[++index]
	user.number = info[++index]
	user.ssn = info[++index]
	user.position = info[++index]
	user.jobType = info[++index]
	user.clearance = calculateClearance(user.jobType) #1 = boss/admin/hr, 2 = regular user, 3 = deactivated
	user.finance = user.finance + "finance.txt" #name of text file
	user.timeCard = user.emplid + "timecard.txt" #name of text file
	createFile(user.finance)
	createFile(user.timeCard)
	return user

def editUser(user, emplid, info):
	if (user.clearance != 3) #deactivated user; cannot edit
		print "Sorry, you are deactivated\n"
	elif (user.emplID == emplid or user.clearance == 1) : #user or admin editing profile
		index = 0

		if (info[index])T
			user.emplID = info[index]
		elif (info[++index])
			user.firstName = info[index]
		elif (info[++index])
			user.lastName = info[index]
		elif (info[++index])
			user.email = info[index]
		elif (info[++index])
			user.password = info[index]
		elif (info[++index])
			user.number = info[index]
		elif (info[++index])
			user.ssn = info[index]
		elif (info[++index])
			user.position = info[index]
		else (info[++index])
			user.jobType = info[index]
			user.clearance = calculateClearance(jobType)
	else :
		print "Sorry, you do not have clearance to edit this profile\n"

def calculateClearance(jobType) :
	if (jobType == boss or jobType == hr)
		clearance = 1
	else
		clearance = 2

def createFile(fileName):
   try:
      file = open(fileName,'w') #create a new file or open one
      file.close()

   except:
      print "Error creating file\n"

def deactivateUser(user)
	user.clearance = 3
	user.position = "deactivated"
	user.jobType = "deactivated"

def recordTime(user)


