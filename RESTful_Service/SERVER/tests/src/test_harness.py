#Importing flask library and its method Flask to initiate Python based Server
#Importing method jsonify to format the return of JSON data in a human friendly format
#Importing method request to check for and parse payload of GET and POST requests to server
#Importing method abort to produce automatic Error handling response in HTML format
#Importing time function to store event times throughout function
#Importing sys to automatically exit program if certain errors received and output message related to error
#Importing os to access relable process kill Ubuntu internal directive
from flask import Flask, jsonify, request, abort, make_response
import time
import sys
import os


#Unneccesary legacy libraries datetime and re when initially performing time calculations in earlier versions
#Soon to be deprecated when all legacy variables will be removed
import datetime
import re


#Declaring chats array which will contain data for unexpired chat/ids which will be returned
chats = []
#Declaring expired_chats array which will hold expired chat/id data
expired_chats = []
#Declaring expiration_times_array which will hold the expiration times for the associated chat/ids
expiration_times_array = []
#Declare chats_username_array
chats_username_array = []
#Declare chats_username_expire_id_array
chats_username_expire_id_array = []
#LEGACY VARIABLE - Declaring variable recur formerly used to find current time and date and perform calculation to see whether chat/ids should be expired
#Variable recur essential for current iteration of script only for while loop which emcompasses entire script -- will remove
recur = list(re.findall('([\d]+):([\d]+):([\d]+)', str(datetime.datetime.now())[:19])[0])



def main():
	try:
		while recur != []:			
			#Initiating Flask python server instance
			app = Flask('__main__')
	

			#Declaring sub-route/path foreign hosts will use to interact with REST Service /chat/username/text endpoint
			#The @ denotes a Python decorator
			#Decorators modify functions immediately following them 
			#Using Python's Flask library, the decorator along with the function definition make a single code block -- if not together an error will occur
			@app.route('/chat/<string:username>/<string:text>', methods=['POST'])
			def add_to_chats(username,text,timeout_1=60):
				if not request.json:
					abort(400)
					
				#Taking the current time which will be used to produce the message ttl(time to live)/timeout/expiration time
				current_time = time.time()
				
				
				#If JSON element timeout specified in data passed, set variable timeout_1 equal to that value
				#Variable timeout_1 to create and expiration time for currently queried chat message
				try:
					timeout_1 = int(request.json["timeout"])
				#If JSON element timeout not found or not parsable, set timeout_1 to integer 60 (although a default value for timeout_1 declared above)
				except:
					timeout_1=60
				
				
					
				#Declaring the variable expiration_time which will hold the amount of seconds before a message expires
				expiration_time = current_time+timeout_1
				
				
				
				#Appending the expiration_time to the times2 array which will be used to monitor the expiration period for every associated chat added
				expiration_times_array.append(expiration_time)
						
					
					
				#Because each chat message will move between two arrays and should never exist in both simultaneously, declare the variable count which will hold the numerical concurrent ID of each message based on the sum of the total lengths of [unexpired] chats array and the expired chats array arrays
				count = len(chats)+len(expired_chats)
				
				
				
				#Construct variable add_chat, which holds data for individual chats, using arguments to add_to_chats function and times associated with with each chat stored in the expiration_times_array
				for i in range(len(expiration_times_array)):
					try:
						add_chat = {"username":username,"text":request.json["text"],"timeout":expiration_times_array[i]-current_time,"id":count}
					except:
						sys.exit('JSON portion of request formatted improperly')
							
							
				#Add formatted chat to unexpired chats list
				chats.append(add_chat)
				

				#Perform calculation of how many seconds chat has to live/is unexpired
				#Done by taking the chat/ids' associated expiration time and subtracting that from the current time
				for i in range(len(expiration_times_array)):
					chats[i]["timeout"]=expiration_times_array[i]-current_time
				
				
				#If chat/id exists, find associated expiration time in expiration_times_array and move it to expired_chats array if expiration time equal to or below 0 (is negative), and do nothing/keep it in unexpired if timeout still above 0
				if expiration_times_array != []:
					def expire_chat():
						if expiration_times_array != []:
							#Use embedded for loop with break statement to reset the value of length of arrays to account for elements deleted
							for i in range(len(expiration_times_array)):
								for ii in range(len(expiration_times_array)):
									if chats[ii]["timeout"] <= 0:
										expired_chats.append(chats[ii])
										del chats[ii]
										del expiration_times_array[ii]
										break
					expire_chat()
				
				
				#times1.append(list(re.findall('([\d]+):([\d]+):([\d]+)', str(datetime.datetime.now())[:19])[0]))
				#if times1 != []:
					#def remove_task():
						#print('1111')
						#print('times1')
						#print(times1)
						#print('2222')
						#print('chats')
						#print(chats)
						#if times1 != []:
							#for i in range(len(times1)):
								#for ii in range(len(times1)):
									#if list(re.findall('([\d]+):([\d]+):([\d]+)', str(datetime.datetime.now())[:19])[0])[1] != times1[0][1] and ((int(list(re.findall('([\d]+):([\d]+):([\d]+)', str(datetime.datetime.now())[:19])[0])[2]) > int(times1[0][2])) or (times1[ii][2] == '59' and int(list(re.findall('([\d]+):([\d]+):([\d]+)', str(datetime.datetime.now())[:19])[0])[1]) >= int(times1[0][1])+2) or (int(list(re.findall('([\d]+):([\d]+):([\d]+)', str(datetime.datetime.now())[:19])[0])[1]) > (int(times1[0][1])+1))):
										#expired_chats.append(chats[ii])
										#del chats[ii]
										#del times1[ii]
										#break
					#remove_task()
					
					
				return jsonify({"chats": chats})

			
			
			
			#Declaring sub-route/path foreign hosts will use to interact with REST Service /chat/id endpoint
			@app.route('/chat/<int:id>', methods=['GET'])
			def return_chats_id(id):
				#Before running function to get chat/id info assure that the id is in the correct area (expired vs. unexpired)
				#Function dependent on chat/id having been queried by API meaning it's timeout and information currently exists
				
				
				#Taking current time which will be used to determine if chat needs to be expired
				current_time = time.time()
				
				#Perform calculation of how many seconds chat has to live/is unexpired
				#Done by taking the chat/ids' associated expiration time and subtracting that from the current time
				for i in range(len(expiration_times_array)):
					chats[i]["timeout"]=expiration_times_array[i]-current_time
				
				#If chat/id exists, find associated expiration time in expiration_times_array and move it to expired_chats array if expiration time equal to or below 0 (is negative), and do nothing/keep it in unexpired if timeout still above 0
				if expiration_times_array != []:
					def expire_chat():
						if expiration_times_array != []:
							#Use embedded for loop with break statement to reset the value of length of arrays to account for elements deleted
							for i in range(len(expiration_times_array)):
								for ii in range(len(expiration_times_array)):
									if chats[ii]["timeout"] <= 0:
										expired_chats.append(chats[ii])
										del chats[ii]
										del expiration_times_array[ii]
										break
					expire_chat()
				
			
			
				#Checking both the unexpired and expired arrays to see if the specified id exists within them
				for i in range(len(chats)):
					if chats[i]["id"] == id:
						return jsonify({"chats": chats[i]})
				for i in range(len(expired_chats)):
					if expired_chats[i]["id"] == id:
						return jsonify({"expired_chats": expired_chats[i]})
			
			
			
			
			#Declaring sub-route/path foreign hosts will use to interact with REST Service /chat/id endpoint
			@app.route('/chats/<string:username>', methods=['GET'])
			def return_chats_username(username):
				chats_username_array = []
				chats_username_expire_id_array = []
				chats_username = ''
			
				#Before running function to get chat/id info assure that the id is in the correct area (expired vs. unexpired)
				#Function dependent on chat/id and username having been queried by API meaning it's timeout and information currently exists
				
				
				#Taking current time which will be used to determine if chat needs to be expired
				current_time = time.time()
				
				#Perform calculation of how many seconds chat has to live/is unexpired
				#Done by taking the chat/ids' associated expiration time and subtracting that from the current time
				for i in range(len(expiration_times_array)):
					chats[i]["timeout"]=expiration_times_array[i]-current_time
				
				#If chat/id exists, find associated expiration time in expiration_times_array and move it to expired_chats array if expiration time equal to or below 0 (is negative), and do nothing/keep it in unexpired if timeout still above 0
				if expiration_times_array != []:
					def expire_chat():
						if expiration_times_array != []:
							#Use embedded for loop with break statement to reset the value of length of arrays to account for elements deleted
							for i in range(len(expiration_times_array)):
								for ii in range(len(expiration_times_array)):
									if chats[ii]["timeout"] <= 0:
										expired_chats.append(chats[ii])
										del chats[ii]
										del expiration_times_array[ii]
										break
					expire_chat()
				
			
			
				#Checking both the unexpired and expired arrays to see if the specified id exists within them
				for i in range(len(chats)):
					if chats[i]["username"] == username:
						chats_username_array.append({"id": chats[i]["id"], "text":chats[i]["text"]})
						chats_username_expire_id_array.append(chats[i]["id"])
					
					
				#Setting name of username to return	
				chats_username = "Chats of user: %s" % username
				
				
				#If chat/id exists, find associated expiration time in expiration_times_array and move it to expired_chats array if expiration time equal to or below 0 (is negative), and do nothing/keep it in unexpired if timeout still above 0
				if chats_username_expire_id_array != []:
					def expire_chat_username():
						if chats_username_expire_id_array != []:
							#Use embedded for loop with break statement to reset the value of length of arrays to account for elements deleted
							for i in range(len(chats_username_expire_id_array)):
								for ii in range(len(chats)):
									if chats[ii]["id"] == chats_username_expire_id_array[i]:
										expired_chats.append(chats[ii])
										del chats[ii]
										del expiration_times_array[ii]
										break
					expire_chat_username()
				
				
				return jsonify({chats_username: chats_username_array})
			
			
	
			#Running app instance of Flask with Debugging if there is an error
			#When the run method of the object of the Flask class is called, it automatically executes functions decorated with the object name
			app.run(host='0.0.0.0', debug=True, port=****)
	except:
		os.system('pkill -9 python')


#Calling main function to initiate script
main()
