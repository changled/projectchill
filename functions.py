import sys

def makeUser(emplid, first, last, email, password, number, ssn, position, finance, jobType):
   user = User()
  	user.emplID = emplid
	user.firstName = first
	user.lastName = last
	user.email = email
	user.password = password
	user.number = number
	user.ssn = ssn
	user.position = position
	user.jobType = jobType
	user.clearance = calculateClearance(jobType)
	user.finance = finance + "finance.txt" #name of text file
	user.timeCard = emplid + "timecard.txt" #name of text file
	createFile(user.finance)
	createFile(user.timeCard)
	return user

def editUser(user, emplid):
	if (user.emplID == emplid or user.clearance == 1) : #user or admin editing profile
		
	else :
		print "Sorry, you do not have clearance to edit this profile"

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
      print "Error creating file"
