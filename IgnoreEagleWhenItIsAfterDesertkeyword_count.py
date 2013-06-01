#By: Aniket Karmarkar
#Date: 8/29/2012
#Description: The following file will take a file with keywords as first input and file which lists path as second input and output a csv file
#which shows the count of each term in the file.
#Notes: 
 
import urllib
import re
import csv

#Create and open csv file for output
#-----------------------------------
keyword_counts =  csv.writer(open("keyword_count_eagle.csv", "wb"))


#Get list of terms from text file
#--------------------------------
FILE	= open('E:\Dropbox\HiphopFiles\Python Script\Counts Program/Eagle.txt', 'r')
terms	= FILE.readlines()
terms	= [term.split('||') for term in terms]	# Parse with || delimiter
terms	= [term for sublist in terms for term in sublist]	# Flatten nested lists
terms	= [term.strip() for term in terms]	# Remove whitespaces
terms	= [term.lower() for term in terms]	# Convert to lowercase
FILE.close()
terms.sort()
keyword_counts.writerow(terms)
tracks = []
print(terms)
print("-------------------------")
print("-------------------------")
# Get list of each track lyric text files
# ---------------------------------------
FILE = open('E:\Dropbox\HiphopFiles\Python Script\Counts Program\SourcePathNew.txt', 'r')
for line in FILE:
    line = line.replace("\n","")
    tracks.append(line)
FILE.close()

# For every track get count of words that match keywords
# ------------------------------------------------------

for track in tracks:
    # a. Get track data
    FILE	= open(track, 'r')
    lines	= FILE.readlines()
    lines = [line.lower() for line in lines]
    FILE.close()
    counts = {}
    for term in terms:
        for line in lines:
            #matches = re.findall('[\W]*'+term+'[e]*[s]*[^a-zA-Z0-9_\,\/]', line, re.IGNORECASE)
            matches = re.findall('\\b'+'(?<!desert) eagle '+'\\b',line, re.IGNORECASE)
            if term in counts:
                counts[term] = counts[term] + len(matches)
            else:
                counts[term] = len(matches)
    #convert to list
    count = sorted(counts.items())
    outputCount = []
    for NumberOfTerms in range(0,len(count)):
        outputCount.append(count[NumberOfTerms][1])
    if max(outputCount) > 0:
        outputCount.append(track.replace("E:/University of Chicago Hip Hop Lyrics Project/","http://lyrics.chicagobooth.edu/"))
        keyword_counts.writerow(outputCount)

print('Huzza!')

##for track in tracks:
##    #read in raw string
##    raw = urllib.urlopen(track).read()
##    #break up string into words and punctuations
##    tokens = nltk.word_tokenize(raw)
##    tokens = [token.lower() for token in tokens]
##    #convert to text for processing with nltk
##    text = nltk.Text(tokens)
##    for term in terms:
##        xx = '<'+term+'>'
####        print(xx)
##        print(term)
##        print(text.findall(xx))
##    
##
