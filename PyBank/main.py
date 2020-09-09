# PyBank
import os
import csv
import datetime

#filepath
csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")

#initialize variables
NetTotal = 0.0
TotalChanges = 0.0
Lastrow = 0.0
AverageProfitLoss = 0.0
GreatestIncrease = 0.0
GreatestDecrease = 0.0
GreatestIncreaseMonth = 'N/A'
GreatestDecreaseMonth = 'N/A'

length = 0  #number of rows of data

with open(csvpath) as csvfile:

    bankdata = csv.reader(csvfile,delimiter = ",")

    next(bankdata)  #skip header row
    for row in bankdata:
        length = length + 1 #count data rows
        NetTotal = NetTotal + int(row[1])   #add each new row to total
        TotalChanges = TotalChanges + (int(row[1])-Lastrow) #find change from last row and add to change total
        Lastrow = int(row[1])   #set last row before iteration
        

        #check if new row increase is greater
        if GreatestIncrease < int(row[1]):
            GreatestIncrease = int(row[1])
            GreatestIncreaseMonth = row[0]

        #check if new row decrease is greater
        if GreatestDecrease > int(row[1]):
            GreatestDecrease = int(row[1])
            GreatestDecreaseMonth = row[0]
    
    AverageProfitLoss = TotalChanges/length 

    #format outputs
    GreatestDecreaseOut = "${:.0f}".format(GreatestDecrease)
    GreatestIncreaseOut = "${:.0f}".format(GreatestIncrease)
    NetTotalOut = "${:.0f}".format(NetTotal)
    AverageProfitLossOut = "${:.2f}".format(AverageProfitLoss)

#format each output line and assign to arbitrary variable
a = "Financial Analysis"
b = '-------------------------'
c = f'Total Months: {length}'
d = f'Total: {NetTotalOut}'
e = f'Average Change: {AverageProfitLossOut}'
f = f'Greatest Increase in Profits: {GreatestIncreaseMonth} ({GreatestIncreaseOut})'
g = f'Greatest Decrease in Profits: {GreatestDecreaseMonth} ({GreatestDecreaseOut})'

print(f'{a}\r\n{b}\r\n{c}\r\n{d}\r\n{e}\r\n{f}\r\n{g}') #print all outppput lines with newline between

outputdata = [a,b,c,d,e,f,g]    #combine list of all output


outputpath = os.path.join('..','PyBank','analysis','PyBank_Summary.txt')

with open(outputpath,'w') as outputfile:
    for x in outputdata :
        outputfile.write(x)         #write each line in the list
        outputfile.write('\r\n')    #write newline

