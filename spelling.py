from nelsonfunctions import *
from enchant import *

def openfromsourcedoc():
	stem = "C:\\cygwin\\home\\nelson auner\\Pontikes\\FinalData.OctNewKeepAndAnonymous"
	sourcedoc = "C:\\Users\\nelson auner\\Dropbox\\HiphopFiles\\Python Script\\SourceswithArtist.csv"
	sourcefile = open(sourcedoc,'r')
	for s in sourcefile.read().splitlines():
		splitsource = s.split(",")
		song = splitsource[1]
		return stem+"\\"+song

def something():
	song = openfromsourcedoc()
	raw = file.read()
	outputfile = open("C:\\Users\\nelson auner\\Desktop\\troubleshooting.txt","w")
	buzzwords = ["typed","artist:","album:","title:","song:"]
	tb = removesonginfo(tb,15,buzzwords)
	tb = removebrackets(tb)
	tb = " ".join(tb) #since removesonginfo returns a list of strings
	tb = tb.lower() #convert put back into one string, to all lower case
	outputfile.write(tb+"\n")
	#tb = tb.translate(string.maketrans("",""), string.punctuation) #remove ending puctuation
	#tb = tb.replace("\n"," ")
	punctuation = re.compile(r'[.?!,\":;]')  #This nukes all punctuation and numbers
	tb = punctuation.sub("", tb)
	#No need to take out stopwords yet - this is handled by the parser itself -- maybe
	tb.split(" ")
	return(tb)

def checkstemmers():
	raw = customparse("C://cygwin//home//nelson auner//Pontikes//FinalData.OctNewKeepAndAnonymous/capsavem/my_cape/outtoget.cap.txt")
	wordz = raw.split(" ")
	O = ["sweating","tripping","gunning","going"] 
	HH = [i[0:-1] for i in O] 
	dic = enchant.Dict("en_US") 
	from nltk import LancasterStemmer, PorterStemmer
	lancaster = LancasterStemmer()
	porter = PorterStemmer()
	resporter = [porter.stem(t).replace(" ","") for t in wordz] 
	reslan = [lancaster.stem(t).replace(" ","") for t in wordz]
	resall = [[wordz[i],resporter[i],reslan[i]]  for i in range(len(wordz)) ]
	filtres = [resall[i] for i in range(len(resall)) if not (resall[i][0]==resall[i][2]==resall[i][1])]
	return resall



def colprint(filename,lls):
	#must be more than 1 column to print
	output = open(filename,"w")
	for i in range(len(lls)):
		for j in range(len(lls[1])):
			output.write(lls[i][j]+"|")
		output.write("\n")
