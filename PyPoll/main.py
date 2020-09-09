#PyPoll
import os
import csv

#filepath
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

#initialize variables
Votescast = 0
candidates = ['Khan','Correy','Li','O\'Tooley']
candidatepercent=[0.0,0.0,0.0,0.0]
candidatevotes=[0,0,0,0]
winningcandidate = ""
x = 0



with open(csvpath) as csvfile:
    votedata = csv.reader(csvfile,delimiter = ",")

    next(votedata)
    for row in votedata:
        # if row[2] not in candidates:   #finds unique names of candidates and appends them to list
        #     candidates.append(row[2])
        Votescast = Votescast+1
        if row[2] ==candidates[0]:
            candidatevotes[0]+=1
        elif row[2] == candidates[1]:
            candidatevotes[1]+=1
        elif row[2] == candidates[2]:
            candidatevotes[2]+=1
        elif row[2] == candidates[3]:
            candidatevotes[3]+=1
    
    # for x in range(len(candidates)):
    #     for vote in votedata:
    #         Votescast = Votescast+1
    #         if str(vote[2]) == str(candidates[x]):
    #             candidatevotes[x]+=1

    #calculate and format percentages of vote for each candidate
    for x in range(len(candidatevotes)):
        candidatepercent[x] = "{:.3f}%".format((candidatevotes[x]/Votescast)*100)
    
#for finding the winner, picks out the highest value and returns the index    
index_max = max(range(len(candidatevotes)),key=candidatevotes.__getitem__)
winningcandidate = candidates[index_max]

#format each output line and assign to arbitrary variable
a = "Election Results"
b = '-------------------------'
c = f'Total Votes: {Votescast}'
d = '-------------------------'
e = f'{candidates[0]}: {candidatepercent[0]} ({candidatevotes[0]})'
f = f'{candidates[1]}: {candidatepercent[1]} ({candidatevotes[1]})'
g = f'{candidates[2]}: {candidatepercent[2]} ({candidatevotes[2]})'
h = f'{candidates[3]}: {candidatepercent[3]} ({candidatevotes[3]})'
i = '-------------------------'
j = f'Winner: {winningcandidate}'
k = '-------------------------'

outputdata = [a,b,c,d,e,f,g,h,i,j,k]    #combine list of all output

for line in outputdata:     #print all output to terminal
    print(f'{line}')

outputpath = os.path.join('..','PyPoll','analysis','Vote_Summary.txt')

with open(outputpath,'w') as outputfile:
    for x in outputdata :
        outputfile.write(x)         #write each line in the list
        outputfile.write('\r\n')    #write newline