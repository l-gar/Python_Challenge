import os
import csv

budget_data = "C:\\Users\\Jorge\\Desktop\Python_Challenge\\PyBank\\Resources\\budget_data.csv"


t_months = 0
t_revenue = 0


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    rows = []
    p = []
    months = []
    
    for i, row in enumerate (csvreader):
            if i == 0:
                header = row
            else:
                rows.append(row)
                p.append(int(row[1]))
                months.append(row[0])
                
                t_months = t_months + 1
                t_revenue = t_revenue + int(row[1])
    
    avg_change = []
                
    for x in range(1,len(p)):
        avg_change.append((int(p[x]) - int(p[x-1])))
        
    r_avg = sum(avg_change)/len(avg_change)
    
    max_increase = max(avg_change)
    max_decrease = min(avg_change)

                
                                
print("Financial Analysis")
print("---------------------------------------------------------")
print ("Total Months: " + str(t_months))
print ("Total: $" + str(t_revenue))
print ("Average Change: $" + str(r_avg))
print("Greatest Increase in profits: " + str(months[avg_change.index(max(avg_change)) + 1]) + " ($" + str(max_increase) +")")
print("Greatest Decrease in Profits: "+ str(months[avg_change.index(min(avg_change)) + 1]) + " ($" + str(max_decrease) + ")")

file = open("output.txt", "r+")
file.write("Financial Analysis")
file.write("\n---------------------------------------------------------")
file.write("\nTotal Months: " + str(t_months))
file.write("\nTotal: $" + str(t_revenue))
file.write("\nAverage Change: $" + str(r_avg))
file.write("\nGreatest Increase in profits: " + str(months[avg_change.index(max(avg_change)) + 1]) + " ($" + str(max_increase) +")")
file.write("\nGreatest Decrease in Profits: "+ str(months[avg_change.index(min(avg_change)) + 1]) + " ($" + str(max_decrease) + ")")
file.close()