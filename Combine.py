#By: Nelson Auner
#Date

import os
from nelsonfunctions import nelsonlinewrite
path = os.getcwd()

file = path+'\\top_20_words_per_lyric_file.csv'
outfile = path+'\\combinedoutputtop20.txt'

#This will create unique list from list. Could have been fast in C...oh well. 
def f5(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result


def readFileAndStrip(filename,stripnum):
	data = [x.strip().split('|') for x in open(filename)]#[stripnum:-1]
	newdata = [[x[1:-1]] for x in data]
	return newdata



def go():
	data=readFileAndStrip(file,1)
	fdata = [item for sublist in data for item in sublist]
	fdata = [item for sublist in fdata for item in sublist]	#flatten data
	udata = f5(fdata) #unique data
	nelsonlinewrite(udata,outfile,"a")
	return(udata)
	
go()