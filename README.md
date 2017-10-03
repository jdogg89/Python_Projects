# Filepathsize.py Synopsis:
The filepathsize.py python program(written with python3 syntax in mind) will list the files under a specific linux(tested on Amazon Linux ec2 instance) or unix(tested on MacOS) mount and return the file path of the file plus its size in bytes. The code, including comments is below.

Run this command to execute the program: "python filepathsize.py [mount point]", example: python filepathsize.py /tmp. 

The output of the program can be viewed in filepathsize_output.txt within the Python_Project folder.
 
# Scaling to Production
A high disk utilization alert could trigger the filepathsize.py program to be executed. The output of the program would be piped to an HTML file and viewed at an internally accessible HTML page. With this solution, whenever disk space becomes an issue the high disk usage files can quickly be identified and removed based on necessity.

A potential solution for promoting the Python program from an initial development environment would be through Chef. Place the code into version control and upon updates to a git repo, Chef server could automatically pick up updates via a github webhook and curl command calling a Jenkins job for chef server updates to role files. When the nodes (servers) communicate to chef server, via heartbeat, they can pickup the program upon inital bootstrap to Chef server and any subsequent updates. 



# Working Code

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/python
#Import necessary modules for program
import os
import json
import sys
#Test is given to ensure that input given at terminal is acceptable
try:
#Mount global variable given as an input with argv command
    mount = str(sys.argv[1])
except IndexError:
    print ("Give mount point as arugments")
    sys.exit()
#Populate dictionary with filesize and filename + path
data = dict()
#Using os.walk to generate filenames in the folder tree, taking the mount variable
for root, directories, filenames in os.walk(mount):
    for filename in filenames:
        #Setting filepath and filesize variables
        file_path = os.path.join(root,filename)
        file_size = os.path.getsize(file_path)
        #Updating data into dictionary
        data.update({file_path:file_size})
        #Converting output of dictionary to json and outputting this to the terminal
        j = json.dumps(data)
print (j)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
