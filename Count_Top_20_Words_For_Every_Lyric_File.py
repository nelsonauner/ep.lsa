#By: Aniket Karmarkar
#Date: 9/26/2012
#Description: The following file will print the top 20 words for every file 

import nltk 
import urllib
import csv
from nltk.corpus import stopwords

#Create and open csv file for output
#-----------------------------------
top_20_words =  csv.writer(open("top_20_words_per_lyric_file.csv", "wb"))
tracks = []

# Get list of each track lyric text files
# ---------------------------------------

#------------------NELSON---------------------------------------
import os
from itertools import chain
from nelsonfunctions import inforemove,infocheck,nelsonlinewrite
#------------------MODIFY HERE-----------------------------------
path = os.getcwd()+'\\Counts Program\\SourcePath.txt'
infobuzzwords = ["typed","artist","album","title","song"]
stopwords = nltk.corpus.stopwords.words('english')
outfile = "top_20_words_per_lyric_file.csv"
#------------------------------------------------------

stopwords.extend([x.strip() for x in open("newstopwords.txt.")]) #combine with new words


FILE = open(path, 'r')
for line in FILE:
    line = line.replace("\n","")
    tracks.append(line)
FILE.close()

# For every track get count of words that match keywords
# ------------------------------------------------------

word = []

for track in tracks:
	word = [] #Clear word buffer
	#read in raw string
	raw = urllib.urlopen(track).read()
	##EDITS BY NELSON: take apart, remove artist etc, put back together with spaces
	lines =' '.join(inforemove(raw.split('\n'),infobuzzwords,10))
	#break up string into words and punctuations
	tokens = nltk.word_tokenize(lines)
	#convert to text for processing with nltk
	text = nltk.Text(tokens)
	#get frequency distribution
	fdist = nltk.FreqDist(text)
	#get distinct items from text
	vocab = fdist.keys()
	word.extend([track])
	#remove stopwords from vocab list
	content = [w for w in vocab if w.lower() not in stopwords]
	word.extend(content[:20])
	#write out top 20 words
	nelsonlinewrite(list(chain(word)),outfile,"a")
	#top_20_words.writerow(word)

print('Huzza!')
    
