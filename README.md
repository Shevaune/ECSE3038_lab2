# ECSE3038_lab2
# Aim of Lab
This lab is an exercise which is aimed to get students more accustomed to the different technologies used in designing and implementing a RESTful API server.
# Program Description
This project will be used to manage a system that monitors the status of a set of electronically measured water tanks. The embedded circuit that is attached to each water tank will measure the height of the water in the tank and report on the tank's current occupancy as a percentage of its maximum capacity.
# Requirements 
1. It is required to design a RESTful API which allows each IoT enabled water tank to interface with the server so that the measured values can be represented visually on a web page. 
2. The API should also support the maintenance of a simple user profile.
3. The server should be able to perform the actions of a simple HTTP web server. The server should be able to perform actions on a resource such as Create, Read, Update and Delete which is to be done without the use of a database.
4. The server should be designed to host at least 7 specific HTTP routes. 
# Function Description
# Profile routes
1. GET /profile

The server should allow a user to create only one user profile. The get request should only return a singular JSON object.

2. POST /profile
The server should allow for an incoming post request that accepts a JSON body as described. The server response should be structured as the "Expected Response". 

3. PATCH /profile
The server should allow a user to alter the parts of the profile after it has been posted. The server should allow the requester to make a JSON body with any combination of the three attributes and update them as necessary. 

# Data Routes
1. GET /data
This route should return an array of 0 or more objects. A newly deployed server should return an empty array.  If a POST request was successfully made to the /data route previously, the GET route should return the posted object in the array. 

2. POST /data
This route should accept a JSON structured. On success, the server should respond to the same JSON that was posted with the addition of an `id` attribute which is to be generated by the server. 

3. PATCH /data/:id
The server should allow a user to alter the parts of one of the tanks after it has been posted. The server should allow the requester to make a JSON body with any combination of the four attributes and update them as necessary.

4. DELETE /data/:id
The server should allow the requester to delete any previously POSTed object. 

# Joke
Why should the number 288 never be mentioned? It’s two gross :) 
