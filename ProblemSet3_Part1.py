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

#%% Task 3 - Lists and Iteration 

#Create empty list variable 
user_numbers = []

#Add user_integer to user_numbers
for user_integer in range(3):
    #Use input function to ask for an integer (and make an integer using int())
    user_integer = int(input("Enter an integer: "))
    #add inputs to empty list
    user_numbers.append(user_integer)

#sort list in ascending numeric order 
user_numbers.sort()

#print last (highest) value in list
print(user_numbers[-1])

#How I fixed code to return 100, not 20:
#When I originally ran this loop, I did not convert the user input to an integer, meaning that the inputs were all strings. When i tried to use the sort function to numerically sort the numbers, it wouldn't do that because it was reading them as strings, so I had to change it in order to get it to print 100

#%% Task 3 - Challenge
#Create empty list variable 
user_numbers = []

#Add user_integer to user_numbers
for user_integer in range(3):
    #Use input function to ask for an integer (and make an integer using int())
    user_integer = int(input("Enter an integer: "))
    #add inputs to empty list
    user_numbers.append(user_integer)

#sort list in reverse numeric order 
user_numbers.sort(reverse=True)
#print the entire list of values
print(user_numbers)