#PyPoll
import os
import csv

#filepath
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

#initialize variables
Votescast = 0
candidates = []
candidatepercent=[0.0,0.0,0.0,0.0]
candidatevotes=[0,0,0,0]
winningcandidate = ""
w = 0
x = 0
y = 0
z = 0

#this with opens the file to get the list of all unique candidates in the race
with open(csvpath) as csvfile:
    votedata = csv.reader(csvfile,delimiter = ",")
    next(votedata)

    for row in votedata:
        if row[2] not in candidates:   #finds unique names of candidates and appends them to list
            candidates.append(row[2])
        
#this with open the file to count total votes as well as votes for each candidate dynamically based on previous candidate list         
with open(csvpath) as csvfile:
    votedata = csv.reader(csvfile,delimiter = ",")
    next(votedata)

    for vote in votedata:
        Votescast+=1
        for w in range(len(candidates)):
            if vote[2] == candidates[w]:
                candidatevotes[w]+=1
   
#calculate and format percentages of vote for each candidate
for x in range(len(candidatevotes)):
    candidatepercent[x] = "{:.3f}%".format((candidatevotes[x]/Votescast)*100)       

#for finding the winner, picks out the highest value and returns the index    
index_max = max(range(len(candidatevotes)),key=candidatevotes.__getitem__)
winningcandidate = candidates[index_max]

#format each output line and assign to arbitrary variable
outputdata = []
resultsoutput = []

a = 'Election Results'
b = '-------------------------'
c = f'Total Votes: {Votescast}'
d = '-------------------------'
#write a list of strings with all candidate and vote counts
for y in range(len(candidates)):
    resultsoutput.append(f'{candidates[y]}: {candidatepercent[y]} ({candidatevotes[y]})')

i = '-------------------------'
j = f'Winner: {winningcandidate}'
k = '-------------------------'

outputdata = [a,b,c,d]    #combine list of all output
for z in range(len(resultsoutput)):
    outputdata.append(resultsoutput[z])
outputdata.append(i)
outputdata.append(j)
outputdata.append(k)

for line in outputdata:     #print all output to terminal
    print(f'{line}')

outputpath = os.path.join('..','PyPoll','analysis','Vote_Summary.txt')
x = 0
with open(outputpath,'w') as outputfile:
    for x in outputdata :
        outputfile.write(x)         #write each line in the list
        outputfile.write('\r\n')    #write newline