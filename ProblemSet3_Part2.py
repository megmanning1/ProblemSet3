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

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3

#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for datalines in lineList[1:]:
    #Split the data into values
    LineData = datalines.split(",")
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = LineData[mmsi_idx]
    #Extract the fleet value
    fleet = LineData[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet

#check to see if the dict has 1040 items
len(vesselDict)

# %% Task 4.4 

#assign 440196000 to vesselID
vesselID = "440196000"

#Look up fleet value of vesselID number
print(vesselDict[vesselID])

#Print statement
print(f"Vessel # {vesselID} flies the flag of {vesselDict[vesselID]}")

#%% Task 5 

#Open Loitering Dataset
LoiteringObj = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
line_list = LoiteringObj.readlines()

#Release the link to the file objects (now that we have all its contents)
LoiteringObj.close() #Close the file

#Create string of header items
header = line_list[0]
header_string = header.split(",")
print(header_string)

#Create index values for each parameters
transshipment_mmsi_idx = header_string.index("transshipment_mmsi")
starting_lat_idx = header_string.index("starting_latitude")
ending_lat_idx = header_string.index("ending_latitude")
starting_lon_idx = header_string.index("starting_longitude")
ending_lon_idx = header_string.index("ending_longitude")

print(transshipment_mmsi_idx,starting_lat_idx,ending_lat_idx,starting_lon_idx,ending_lon_idx)

#Loop through each line of data (skipping header)
for eachline in line_list[1:]:
    #Split the data into values
    line_data = eachline.split(",")
   
    #Store parameters into own variables 
    #Had issues with data types so converted parameters to floats
    trans_mmsi = line_data[transshipment_mmsi_idx]
    starting_lat = float(line_data[starting_lat_idx])
    ending_lat = float(line_data[ending_lat_idx])
    starting_lon = float(line_data[starting_lon_idx])
    ending_lon = float(line_data[ending_lon_idx])

    #examine start and end lat & create boolean variable if it crosses equator
    crosses_equator = starting_lat < 0 < ending_lat

    #examine start and end lon & create boolean variable if falls in range
    #within_lon_range = starting_lon > 145 and ending_lon < 155
            #tried above originally, but was getting an extra Kiribati vessel so altered to below
    within_lon_range = 145 < starting_lon < 155

    #if both variables are true, query dictionary
    if crosses_equator and within_lon_range:
        fleet_name = vesselDict.get(trans_mmsi)
        if fleet_name:
            print(f"Vessel #{trans_mmsi} {starting_lon} flies the flag of {fleet_name}")
        else:
            print(f"No vessels met criteria")
