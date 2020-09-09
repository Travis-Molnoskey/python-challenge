#PyPoll
import os
import csv

#filepath
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

#initialize variables
Votescast = 0
candidates = []
candidatepercent=[]
candidatevotes=[]
winningcandidate = ""
x = 0

with open(csvpath) as csvfile:
    votedata = csv.reader(csvfile,delimiter = ",")

    next(votedata)
    for row in votedata:
        if row[2] not in candidates:
            candidates.append(row[2])
    
    for x in range(len(candidates)):
        for vote in votedata:
            Votescast = Votescast+1
            if vote[2] == candidates[x]:
                candidatevotes[x]=candidatevotes[x]+1



print(f'{candidatevotes[1]}')

#print(f'{Votescast}')

