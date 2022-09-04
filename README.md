# DevOPS First Task 

*Task 01:*  

- Creating and Initializing Sprints-DevOps Directory with three branches: Dev, Test, Production. In Dev Branh, create function MyFunc() in Sprints.py module that takes a List of Integers and Float and returns the Mean of Even Integers, Max Number of Float Numbers, or 0 if the List contains Neither Integers or Floats.

*Task 02:*  
- In Test Branch, create python file test.py and import sprints.py and call the function and test it with the lists.  
	For hint: https://realpython.com/python-testing/   

*Task 03:*  
- In Production Branch, write a bash script in sshd.sh to get an integer number input from the user to Change the SSH Port (making sure the port is accepted in range), disable root login to system, and make sure that there's at least one user with sudo privilege. Then add the files that are passed from Test.  

*Task 04:*  
- Creating a DockerFile using image python:3.8, setting work directory to /var/src/app, and Copying all the files in local directory to the Docker container.
