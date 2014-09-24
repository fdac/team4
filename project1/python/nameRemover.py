import csv, codecs, unicodedata, re

def output(outfile,one,two,three,four,five,six):
    outfile.write(one)
    outfile.write(',')
    outfile.write(two)
    outfile.write(',')
    outfile.write(three)
    outfile.write(',')
    outfile.write(four)
    outfile.write(',')
    outfile.write(five)
    outfile.write(',')
    outfile.write(six)
    outfile.write('\n')
    
def unicode_csv_reader(unicode_csv_data):
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data))
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]
        
        
def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')
        
def csv_reverser(line):
    temp = line[::-1]
    yield line.split(",")
    
def remove_non_ascii(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

infile = codecs.open('allPublicRepos.csv', encoding='utf-8', mode='r')
outfile = codecs.open('reposNoNames.csv', encoding='utf-8', mode='w')

#temp = infile.readline()
#print temp
#temp2 = temp.replace("\n","")
#print temp2
#temp3 = temp2[::-1]
#print temp3
#temp4 = temp3.split(",")
#print temp4
#scm = temp4[0][::-1]
#print scm

#temp = unicode(infile.readline(),errors='ignore')
temp = infile.readline()
while temp:
    #print temp
    #temp2 = unicode(temp, 'utf-8', 'ignore')
    #decoded_str = temp.decode('utf-8','ignore')
    #temp2 = unicodedata.normalize('NFKD', temp).encode('ascii','ignore')
    #temp2 = remove_non_ascii(temp)
    temp2 = re.sub(r'[^\x00-\x7F]+','',temp)
    #print temp2
    temp3 = temp2.replace("\n","")
    temp4 = temp3[::-1]
    temp5 = temp4.split(",")
    if(len(temp5) >= 6):
        output(outfile, temp5[0][::-1], temp5[1][::-1], temp5[2][::-1], temp5[3][::-1], temp5[4][::-1], temp5[5][::-1])
    temp = infile.readline()

#reader = csv.reader(infile, delimiter=',')
#for row in reader:
#for row in unicode_csv_reader(infile):
    #for i in range(len(row)-1,len(row)-6, -1):
#    print len(row)
#    output(outfile, row[len(row)-1],row[len(row)-2],row[len(row)-3],row[len(row)-4],row[len(row)-5],row[len(row)-6])

