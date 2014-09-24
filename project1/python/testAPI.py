import requests, json, sys, time, re, pickle, codecs
import bs4 as BeautifulSoup

def output(outfile,test):
    outfile.write(test.name)
    outfile.write(',')
    outfile.write(test.owner)
    outfile.write(',')
    outfile.write(test.language)
    outfile.write(',')
    outfile.write(str(test.size))
    outfile.write(',')
    outfile.write(test.updated)
    outfile.write(',')
    outfile.write(test.created)
    outfile.write(',')
    outfile.write(test.repoType)
    outfile.write('\n')
    
def writeHeader(outfile):
    outfile.write('name')
    outfile.write(',')
    outfile.write('owner')
    outfile.write(',')
    outfile.write('language')
    outfile.write(',')
    outfile.write('size')
    outfile.write(',')
    outfile.write('updated_on')
    outfile.write(',')
    outfile.write('created_on')
    outfile.write(',')
    outfile.write('scm')
    outfile.write('\n')

class repo:
    name = ""
    owner = ""
    language = ""
    size = ""
    updated = ""
    created = ""
    repoType = ""

#URL = 'https://api.bitbucket.org/2.0/repositories'
#URL = 'https://api.bitbucket.org/2.0/repositories?after=2008-08-11T09%3A54%3A13.224236%2B00%3A00&page=10'
#URL = 'https://api.bitbucket.org/2.0/repositories?after=2011-01-19T12%3A58%3A34.687525%2B00%3A00&page=3493'
URL = 'https://api.bitbucket.org/2.0/repositories?after=2011-01-20T12%3A12%3A42.620663%2B00%3A00&page=3502'
r = requests.get(URL)
t = r.text
json_obj = json.loads(t)
firstFlag = 1
#outfile = open('allObjects.csv','w')
outfile = codecs.open('allObjectsv2.csv', encoding='utf-8',mode='a')
#writeHeader(outfile)
#print json_obj['pagelen']
numresults = json_obj['pagelen']
for res in range(0, numresults):
    test = repo()
    test.name = json_obj['values'][res]['name']
    test.owner = json_obj['values'][res]['owner']['username']
    test.language = json_obj['values'][res]['language']
    test.size = json_obj['values'][res]['size']
    test.updated = json_obj['values'][res]['updated_on']
    test.created = json_obj['values'][res]['created_on']
    test.repoType = json_obj['values'][res]['scm']
    #if(firstFlag == 1):
    #    repoList = [test]
    #else:
    #    repoList.append(test)
    #entry = (test.name, ',', test.owner, ',', test.language, ',', test.size, ',', test.updated, ',', test.created, ',', test.repoType)
    #outfile.write(str(entry))
    #outfile.write(test.name)
    #outfile.write(',')
    #outfile.write(test.owner)
    #outfile.write(',')
    #outfile.write(test.language)
    #outfile.write(',')
    #outfile.write(str(test.size))
    #outfile.write(',')
    #outfile.write(test.updated)
    #outfile.write(',')
    #outfile.write(test.created)
    #outfile.write(',')
    #outfile.write(test.repoType)
    #outfile.write('\n')
    output(outfile,test)
    #print test.name, ',', test.owner, ',', test.language, ',', test.size, ',', test.updated, ',', test.created, ',', test.repoType

#maxIterations = 100
counter = 3501    

nextURL = json_obj['next']
#for pg in range(2, 11):
while nextURL:
    #if(counter >= maxIterations): break
    counter += 1
    print 'page:', counter
    print 'url:', nextURL
    r = requests.get(nextURL)
    t = r.text
    json_obj = json.loads(t)
    numresults = json_obj['pagelen']
    for res in range(0, numresults):
        test = repo()
        test.name = json_obj['values'][res]['name']
        test.owner = json_obj['values'][res]['owner']['username']
        test.language = json_obj['values'][res]['language']
        test.size = json_obj['values'][res]['size']
        test.updated = json_obj['values'][res]['updated_on']
        test.created = json_obj['values'][res]['created_on']
        test.repoType = json_obj['values'][res]['scm']
        #if(firstFlag == 1):
        #    repoList = [test]
        #else:
        #    repoList.append(test)
        #entry = (test.name, ',', test.owner, ',', test.language, ',', test.size, ',', test.updated, ',', test.created, ',', test.repoType)
        #outfile.write(str(entry))
        #if(counter == 125):
        #    print test.name
        #    print nextURL
        output(outfile,test)
        #print test.name, ',', test.owner, ',', test.language, ',', test.size, ',', test.updated, ',', test.created, ',', test.repoType
    nextURL = json_obj['next']
        
outfile.close()