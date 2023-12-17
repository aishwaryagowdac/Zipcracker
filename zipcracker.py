#!/usr/bin/python3
"""imported 3 libraries
zipfile: to create, read, write, and manipulate ZIP files
time: to implement time function
sys: to pass arguments during execution """ 
import zipfile
import time
import sys

#starts the time before the password cracking begins
start_time = time.time()

#Pass zipfile and password list as arguments while running the script 
zfile = sys.argv[1]
dfile = sys.argv[2]
#creates zipfile object 
filezip = zipfile.ZipFile(zfile)
#Opens password file
passfile = open(dfile)
count = 0

"""reads the password file, separates the words using strip
encodes the password string using utf-8"""
for line in passfile.readlines():
	#"\n" is removed for IMPROVED SPEED
	password = line.strip()
	codedpass = bytes(password, 'utf-8')
	#stores number of words that was checked
	count = count + 1
	"""if the password was found, prints the password
	else, prints the password that was attempted"""
	try:
		filezip.extractall(pwd=codedpass)
		print ("[----------Password Found------------] -->" + password)
		print ("Passwords attempted: " + str(count))
		break
	except:
		continue
		#print ("**Attempted Password**" + password)
		#Print line is commented for IMPROVED SPEED 

#ends the timer once the password cracking is done and calculates elapsed time and tries per second and prints it
end_time = time.time()
elapsed_time = end_time - start_time
tries_per_seconds = count / elapsed_time 
print (f"Time consumed: {elapsed_time} seconds")
print ("Passwords attempted: " + str(count) + " At " + str(tries_per_seconds) + " tries per second")
print ("Password cracked for the zip file: " + zfile + " using the password file: " + dfile) 

