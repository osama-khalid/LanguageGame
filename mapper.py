import pickle
import csv

with open('Fruits.obj', 'rb') as fp:
    banana = pickle.load(fp)   
    

senseMap={}    

with open('lexicon_weight.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        senseMap[row[0]]=row[1]    
    
mapper={}    
mapSense={}
totalMaps=[]
with open('conceptMap.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        maps=row[1].split(',')
        for m in maps:
            totalMaps.append(m)
            if int(m) not in mapper:
                mapper[int(m)]=[]
            mapper[int(m)].append(row[0])
            if int(m) not in mapSense:
                mapSense[int(m)]=[]
            mapSense[int(m)].append(senseMap[row[0]])
            
c=[]            
for m in mapSense:
    if len(set(mapSense[m]))>1:
        print(m)
        c.append(m)
#3,914 out of 34,579 concepts have multiple senses e.g. yawn and yawning



#how do you resolve ambiguity, can we take the average scores?            