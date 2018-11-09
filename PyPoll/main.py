#Import os and csv
import os
import csv

#connect to file using file path
election_data = "C:\\Users\\Jorge\\Desktop\\Python_Challenge\\PyPoll\\Resources\\election_data.csv"

#create lists that will hold data to use later
candidatelist = []
unique_candidate = []
v_count = []
v_percent = []

#open the csv file into the program
with open(election_data) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #this will hold all data withouth header
    rows = []
    
    for i, row in enumerate(csvreader):
        if i == 0:
            header = row
        else:
            rows.append(row)
            candidatelist.append(row[2])
            
    total_V = len(rows)   
    
    for x in set(candidatelist):
        unique_candidate.append(x)
        
        t_v_candidate = candidatelist.count(x)
        
        v_count.append(t_v_candidate)
        
        p_v_percent = (t_v_candidate/total_V)*100
        v_percent.append(p_v_percent)
    
    winning_v_count = max(v_count)
    winner = unique_candidate[v_count.index(winning_v_count)]
    
             
            

print("Election Results")
print("----------------------------------")
print("Total votes: " + str(total_V))
print("----------------------------------")
print(unique_candidate[1] + ": " + str(round(v_percent[1],4)) + "% (" + str(v_count[1])+ ")")
print(unique_candidate[0] + ": " + str(round(v_percent[0],4)) + "% (" + str(v_count[0])+ ")")
print(unique_candidate[2] + ": " + str(round(v_percent[2],4)) + "% (" + str(v_count[2])+ ")")
print(unique_candidate[3] + ": " + str(round(v_percent[3],4)) + "% (" + str(v_count[3])+ ")")
print("----------------------------------")
print("Winner: " + winner)
print("----------------------------------")

file = open("output.txt", "r+")
file.write("Election Results")
file.write("\n----------------------------------")
file.write("\nTotal votes: " + str(total_V))
file.write("\n----------------------------------")
file.write("\n" + unique_candidate[1] + ": " + str(round(v_percent[1],4)) + "% (" + str(v_count[1])+ ")")
file.write("\n" + unique_candidate[0] + ": " + str(round(v_percent[0],4)) + "% (" + str(v_count[0])+ ")")
file.write("\n" + unique_candidate[2] + ": " + str(round(v_percent[2],4)) + "% (" + str(v_count[2])+ ")")
file.write("\n" + unique_candidate[3] + ": " + str(round(v_percent[3],4)) + "% (" + str(v_count[3])+ ")")
file.write("\n----------------------------------")
file.write("\nWinner: " + winner)
file.write("\n----------------------------------")