import requests
import json
import time
import sys

#### USER REQUIRED ####

dbhost  = ""
dbname  = ""
dbuser  = ""
dbpass  = ""
phpfile = "http://yoursite.com/file.php"

#######################

easypasshash = "$P$BFSb0XT3mpWiVFRQq92VWyko9.R2nP." # this is the hash for the word password

def GetUser():
	mode = "gu"
	url = phpfile + "?m=" + mode + "&dbh=" + dbhost + "&dbn=" + dbname + "&dbu=" + dbuser + "&dbp=" + dbpass
	print("Getting Users...")
	print("GET URL: " + url + "\n")
	result = requests.get(url)
	users = json.loads(result.text)
	filename = str(time.time()) + ".txt"
	txtfile = open(filename, "w")
	for user in users:
		print("ID: \t" + user["id"])
		txtfile.write("ID: \t" + user["id"] + "\n")
		print("USER: \t" + user["user"])
		txtfile.write("USER: \t" + user["user"] + "\n")
		print("PASS: \t" + user["pass"])
		txtfile.write("PASS: \t" + user["pass"] + "\n")
		print("EMAIL: \t" + user["email"])
		txtfile.write("EMAIL: \t" + user["email"] + "\n")
		print()
		txtfile.write("\n")
		
	print("Saved details to " + filename)
	print()
	txtfile.close()
	
	
	
	
	
	
def ChangeToPass():
	userid = input("Enter the ID of the user you want to change: ")
	mode = "sph"
	url = phpfile + "?m=" + mode + "&dbh=" + dbhost + "&dbn=" + dbname + "&dbu=" + dbuser + "&dbp=" + dbpass + "&uid=" + userid + "&pwh=" + easypasshash
	print("Setting Password of user with ID = " + userid + " to password...")
	print("GET URL: " + url + "\n")
	result = requests.get(url)
	boolresponse = result.text
	if("true" in boolresponse):
		print("Succesfully changed the users password hash")
		print()
	else:
		print("Something went wrong and it may not have worked")
		print()
	
	
def SetPassHash():
	userid = input("Enter the ID of the user you want to change: ")
	passhash = input("Enter the hash you wish to set the users password to: ")
	mode = "sph"
	url = phpfile + "?m=" + mode + "&dbh=" + dbhost + "&dbn=" + dbname + "&dbu=" + dbuser + "&dbp=" + dbpass + "&uid=" + userid + "&pwh=" + passhash
	print("Setting Password of user with ID = " + userid + " to password...")
	print("GET URL: " + url + "\n")
	result = requests.get(url)
	boolresponse = result.text
	if("true" in boolresponse):
		print("Succesfully changed the users password hash")
		print()
	else:
		print("Something went wrong and it may not have worked")
		print()
	
	
	
def RunOption(option):
	if(option == "1"):
		GetUser()
	elif(option == "2"):
		ChangeToPass()
	elif(option == "3"):
		SetPassHash()
	elif(option == "4"):
		print("Goodbye")
		sys.exit()
	else:
		print()
		print("NOT A VALID OPTION")
		print()
	

def Banner():
	print("########################################")
	print("#                                      #")
	print("#      WORDPRESS CONTROLLER v0.1       #")
	print("#                                      #")
	print("########################################")
	
def Menu():
	print()
	print("[1] Get All Users")
	print("[2] Change a Users Password to password")
	print("[3] Set a Users Password Hash")
	print("[4] Exit")
	print()
	option = input("What would you like to do?: ")
	return option

def Main():
	print()
	Banner()
	option = Menu()
	RunOption(option)
	
	
	
	
	
	
	
	
	
	
	
	
Main()