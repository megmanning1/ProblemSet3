#-------------------------------------------------------------
# ProblemSet3_Part2.py
#
# Author: Meg Manning (meg.manning@duke.edu)
# Date:   October 2024
#
#--------------------------------------------------------------
#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents, mode = 'r' to read contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

# %%
