# #!/usr/bin/python
#import necessary modules
import os
import json
import sys
try:
    mount = str(sys.argv[1])
except IndexError:
    print ("Give mount point as arugments")
    sys.exit()
data = dict()
for root, directories, filenames in os.walk(mount):
    for filename in filenames:
        file_path = os.path.join(root,filename)
        file_size = os.path.getsize(file_path)
        data.update({file_path:file_size})
        #print file_path,file_size
        #print (data)
        j = json.dumps(data)
        print (j)
