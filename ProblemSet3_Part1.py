#-------------------------------------------------------------
# ProblemSet3_Part1.py
#
# Author: Meg Manning (meg.manning@duke.edu)
# Date:   October 2024
#
#--------------------------------------------------------------
#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (f"{mountain}, sometimes \ncalled \"{nickname}\",")
#print (f"called \"{nickname}\",")
print (f"is {elevation}' above sea level.")

#%% Task 2 - Lists and Iteration
#Create a variable for data folder and a list of strings
data_folder = r'W:\859_data\triangle'
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

#assign user_item to the string roads.shp
user_item = "roads.shp"

#add roads.shp to data_list
data_list.append(user_item)
print(data_list)

#Loop through data_list and print full windows path of each dataset
for x in data_list:
    print(f"{data_folder}\{x}")
# %%
