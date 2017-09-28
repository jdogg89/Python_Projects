# Filepathsize.py Synopsis:
The filepathsize.py python program(written with python3 syntax in mind) will find the files of a specific linux(tested on Amazon Linux ec2 instance) or unix(tested on MacOS) mount and return the file path of the file plus its size in bytes. The following code below will be broken down, please refer to commented lines:

Run this command to execute the program: "python filepathsize.py [mount point]", example: python filepathsize.py /tmp. 

The output of the program can be viewed in filepathsize_output.txt within the Python_Project folder.
 
# Scaling to Production
While this python program can be executed locally in an SSH session, this does not address how this could be implemented in a production environment with developers needing to run this program. Depending on the implemented monitoring solution, a high disk utilization alert could trigger the filepathsize.py program to be executed and the output of the program be stored in a publically accessible (only on the internal network for developers and support staff) html page. With this solution, whenever disk space becomes an issue the high disk usage files can quickly be identified and removed based on necessity.



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
for root, directories, filenames in os.walk(mount):
    for filename in filenames:
        #Setting filepath and filesize variables
        file_path = os.path.join(root,filename)
        file_size = os.path.getsize(file_path)
        #Updating data into dictionary
        data.update({file_path:file_size})
        #Print file_path,file_size
        #Print (data)
        #Converting output of dictionary to json and outputting this to the terminal
        j = json.dumps(data)
print (j)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
