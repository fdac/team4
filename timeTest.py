from datetime import datetime
import csv, pickle

#testDateStr = '2008-06-25T00:53:00.273366+00:00'

#testTime = datetime.strptime(testDateStr, '%Y-%m-%dT%H:%M:%S.%f+00:00')

#print testTime.year
#print testTime.month
#print testTime.day

#gitCount = 0
#hgCount = 0
gitCount = [0]
hgCount = [0]
dates = ['']

#gitCount.push(0)
#hgCount.push(0)
#dates.push('')


index = 0
#index1.push(0)
#index2.push(0)
currentMonth = 0
firstFlag = 1
reader = csv.reader(open('reposNoNames.csv','r'))
for row in reader:
    if(firstFlag == 1):
        firstFlag = 0
        continue
    try:
        tempDate = datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S.%f+00:00')
    except ValueError:
        tempDate = datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S+00:00')
    if(currentMonth == 0):
        currentMonth = tempDate.month
        dates[0]= str(tempDate.month) + ' ' + str(tempDate.year)
    if(tempDate.month != currentMonth):
        index += 1
        gitCount.append(gitCount[index - 1])
        hgCount.append(gitCount[index - 1])
        currentMonth = tempDate.month
        dates.append(str(tempDate.month) + ' ' + str(tempDate.year))
    if(row[0] == 'git'):
        gitCount[index] += 1
    elif(row[0] == 'hg'):
        hgCount[index] += 1
        
print dates
print gitCount
print hgCount        

pickle.dump(dates,open('datesArray.p','w'))
pickle.dump(gitCount,open('gitArray.p','w'))
pickle.dump(hgCount,open('hgArray.p','w'))
        
