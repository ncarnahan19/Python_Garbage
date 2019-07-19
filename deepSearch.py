# python3

# delUnnededFiles.py - Finds files more than 100 MegaBites
import os, re
fileOfInterestRe = re.compile(r'Python36')
filename = 'C:\\Users\\nrcar'
bigBoiSize = 0
megabyteDiv = 1000000

for bigBoi in os.walk(filename):
    # bigBoiSize = bigBoiSize + os.path.getsize(os.path.join('C:\\', filename))
    # print(bigBoi[0])
    if fileOfInterestRe.search(bigBoi[0]) != None:
       print(bigBoi)
       #print(' is quite large.  ' + str(bigBoiSize / megabyteDiv) + ' megabytes to be exact.' )