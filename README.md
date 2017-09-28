# Python_Projects
The filepathsize.py python program(written with python3 syntax in mind) listed below, and in this Python_Projects folder will find the files of a specific linux(tested on Amazon Linux ec2 instance) or unix(tested on MacOS) mount and return the file path of the file plus its size. The following code below will be broken down, please refer to commented lines: 

View file in raw format in order for formatting to appear correctly.

# #!/usr/bin/python
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
