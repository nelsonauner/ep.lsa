#-------------------------------------------------------------------
#By Nelson Auner - October 2012
#Taken from http://www.puffinwarellc.com/lsa.py
#
# TODO: better parsing (in nelsonfunctions)
# Eliminate words that only appear in one (or two or three) text file. 
#
#


from pylab import *
from numpy import zeros
from scipy.linalg import svd
#following needed for TFIDF
from math import log
from numpy import *
from nelsonfunctions import *
import time

titles = ["The Neatest Little Guide to Stock Market Investing",
          "Investing For Dummies, 4th Edition",
          "The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns",
          "The Little Book of Value Investing",
          "Value Investing: From Graham to Buffett and Beyond",
          "Rich Dad's Guide to Investing: What the Rich Invest in, That the Poor and the Middle Class Do Not!",
          "Investing in Real Estate, 5th Edition",
          "Stock Investing For Dummies",
          "Rich Dad's Advisors: The ABC's of Real Estate Investing: The Secrets of Finding Hidden Profits Most Investors Miss"
          ]
stopwords = ['and','edition','for','in','little','of','the','to']
ignorechars = ''',:'!'''

#---------------------------------------------------------
threshold = 3
#---------------------------------------------------------


class LSA(object):
    def __init__(self, filestem,sourcedoc): 
        self.sourcedoc = sourcedoc #the document that has the list of sources
        self.filestem = filestem #Where is the OctNewKeep stored on your local computer?
        self.stopwords = csw(nltk.corpus.stopwords.words('english'),"newstopwords.txt")
        self.wdict = {} #This will map word -> docs
        self.IDandSources = {}
        self.dcount = -1 #and goes down        
        self.threshold = 1 #A word has to appear in more than 'threshold' documents to be included

    def loadsources(self):
        """ Using self.sourcedoc, finds or creates and ID for each source in the doc, and adds it to the IDandSources dictionary for later parsing"""
        print("starting!")
        sourcefile = open(self.sourcedoc,'r')
        for s in sourcefile.read().splitlines()
            print(s)
            splitsource = s.split(",")        
            print(splitsource)
            if len(splitsource)==2:  #If there is an artistID
                tempID = splitsource[0]
                song = splitsource[1]
            elif len(splitsource)==1: #If there is no artistID, use dcount
                tempID = self.dcount
                song = splitsource[
                self.dcount -= 1
            if tempID in self.IDandSources:
                self.IDandSources[tempID].append(song)
            else:
                self.IDandSources[tempID] = [song]

    def completematrix(self):
    	self.countwdict = self.wdict
    	l = len(self.sources)
    	#self.cm = zeros((len(self.wdict.keys()),len(self.sources)),dtype=numpy.int8)
    	for key in self.countwdict.keys():
    		self.countwdict[key] = listcompressor(list=self.wdict[key],length=l)

    def printcountcsv(self,title,filename):
        print("Printing the countwdict to "+filename)
        out = open(filename+".csv","w")
        l = len(self.sources)
        sourcestoprint = lscleaner(self.sources,[".txt","C:\cygwin\home\nelson auner\Pontikes\FinalData.OctNewKeepAndAnonymous"])
        out.write(csvprintline([title]+sourcestoprint,delim="|"))
        for key in self.wdict.keys():
            #print([key]+(listcompressor(self.wdict[key],l)))
            out.write(csvprintline([key]+(listcompressor(self.wdict[key],l)),delim="|"))
        
    def parseAllSources(self):
        """Go through self.IDandSources and parse each document! """
        stem = self.filestem
        for ID, songsources in self.IDandSources.items():
            for source in songsources:
            	words = customparse(stem+source) #add the local file stem back to the short file stem
                for w in words:
                    if w in self.stopwords:
                        continue
                    elif w in self.wdict:
                        self.wdict[w].append(ID)   
                        #self.docdic[self.dcount].append(w)
                    else:
                        self.wdict[w] = [ID]
    def build(self):
        self.keys = [k for k in self.wdict.keys() if len(set(self.wdict[k])) > self.threshold]
        self.keys.sort()
        #self.vectors = [self.makeVector(tokens) for tokens in self.keys]
        self.A = zeros((len(self.keys), len(self.IDandSources.keys())))
        for i, k in enumerate(self.keys):
            for d in self.wdict[k]:
                self.A[i,d] += 1

    def TFIDFPrint(self):
        limit = 400
        counter = 1
        outpath = open("WordTFIDFnew.txt","w")
        outpath.write("Token|TF|DF|IDF\n")
        numberofdocs=len(IDandSources.keys())
        for word, docs in self.wdict.items():
            df = len(set(docs))
            # if df <= self.threshold:
            #     continue
            #skip a word if it does not meet threshold
            tf = len(docs)
            idf = math.log((numberofdocs)/df) #this won't work with artists...
            outpath.write(word+"|"+str(tf)+"|"+str(df)+"|"+str(idf)+"\n")
            counter+=1
            if counter > limit:
                outpath.close()
                return()

    def tfidfTransform(self,):
        """ Fromhttp://blog.josephwilk.net/projects/latent-semantic-analysis-in-python.html
                With a document-term matrix: matrix[x][y]
            tf[x][y] = frequency of term y in document x / frequency of all terms in document x
            idf[x][y] = log( abs(total number of documents in corpus) / abs(number of documents with term y)  )
                Note: This is not the only way to calculate tf*idf
        """
        rows = len(self.keys)
        cols = self.dcount
        for  row in xrange(rows):
            wordTotal = reduce(lambda x,y: x+y,self.vectors[row])
            for col in xrange(cols):
                self.vectors[row][col] = float(self.vectors[row][col])
                if self.vectors[row][col]!=0:
                    termDocumentOccurences = self.__getTermDocumentOccurances(col)
                    termFrequency = self.vectors[row][col]/float(wordTotal)
                    inverseDocumentFrequency = log(abs(self.dcount/float(termDocumentOccurences)))
                    self.vectors[row][col] = termFrequency*inverseDocumentFrequency
    def newbuild(self,howmany):
        """ Create the vector space for the new documents strings"""
        self.keys = [k for k in self.wdict.keys() if len(set(self.wdict[k])) > self.threshold]
        self.keys.sort()
        #To conserve memory, create list vector by vector. Vectors can be mapped to the original doc by self.sources[/vector#/]
        self.vectors = []
        for sonum in range(0,howmany): #Or put another number here!
            self.vectors.append(self.makeVector(sonum))

    def makeVector(self, ID):
        #use tfidf? 
        vector = [0] * len(self.keys)
        for i in range(0,len(self.keys)):
            word = self.keys[i]
            for num in self.wdict[word]:
                if num == ID:
                    vector[i]+=1
        return(vector)

    def cosine(vector1,vector2):
        """related documents j and q are in the concept space by comparing vectors:
            cosine = (v1 * v2) / (||v1|| ||v2||) """
        return float(dot(vector2,vector2)/(norm(vector1) * norm(vector2)))

    def __getTermDocumentOccurances(self,col):
        termDocumentOccurences=0
        rows = self.keys
        cols = self.dcount
        for n in xrange(rows):
            if self.vectors[n][col]>0:
                termDocumentOccurences+=1
        return termDocumentOccurences
    def calc(self):
        self.U, self.S, self.Vt = svd(self.A)
    def printA(self):
        print 'Here is the count matrix'
        print self.A
    def printSVD(self):
        print 'Here are the singular values
        print self.S
        print 'Here are the first 3 columns of the U matrix'
        print -1*self.U[:, 0:3]
        print 'Here are the first 3 rows of the Vt matrix'
        print -1*self.Vt[0:3, :]

    def compareartists(ID1,ID2):
        return(cosine(makevector(ID1),makevector(ID2)))

    def makeartistgraph(self):
        #for each artist pairing...
        #return the cosine vector
        outfile = open("artistcosine.txt","w")
        #create the top axis. 
        for artistid in IDandSources.keys():
            outfile.write(str(artistid)+"|")
        outfile.write("\n")
        for firstID in IDandSources.keys():
            for otherID in IDandSources.keys()[firstID:-1]:
                v1 = makeVector(firstID)
                print(str(self.cosine(v1,makeVector(otherID)))+"|")
            print("\n")


def constructor():
    """Initiate building an myLSA document"""
    #Construct a myLSA by loading all the sources from the sources var
    #ignorchars not used?
    mylsa = LSA(filestem = "C:\\cygwin\\home\\nelson auner\\Pontikes\\FinalData.OctNewKeepAndAnonymous",
        sourcedoc ="C:\\Users\\nelson auner\\Dropbox\\HiphopFiles\\Python Script\\SourceswithArtistpractice.txt")
    print("unpackingsources")
    mylsa.loadsources()
    print("unpacked. now creating word dic")
    start = time.clock()
    #modify to use a sourcelist, not whole string
    #mylsa.parseAllSources()
    end = time.clock()
    print("done in "+str(end-start)+" seconds, I think")
    return(mylsa)


def lsa_go():
	mylsa.build()
	mylsa.printA()
	mylsa.calc()
	mylsa.printSVD()

print("constructing!")
mylsa = constructor()
# mylsa.keys = [k for k in mylsa.wdict.keys() if len(set(mylsa.wdict[k])) > 2 ]




#-------------RANDOM CODE BELOW-------------------------------------------------------------------
def printkeys():
    outprint = open("wordlistnov.txt","w")
    for i in mylsa.keys:
        outprint.write(i+"\n")
    outprint.close()

#create the diagnostic plots:

def plotting():
    y = [0,0,0]
    y[0] = [0]*1000
    y[1]= [0]*1000
    y[2] = [0]*1000


    for t in [[0,1],[1,5],[2,100]]:
        mylsa.threshold = t[1]+1
        mylsa.build()
        mylsa.newbuild(1000)
        print(len(mylsa.keys))
        for i in range(1,1000):
            y[t[0]][i]=sum(mylsa.vectors[i])
        y[t[0]].sort()

    #now plot all of these 
    plot(y[0],label="threshold = 1" )
    plot(y[1],label="threshold = 2" )
    plot(y[2],label="threshold = 3" )
    legend(loc="upper left")
    show()
#debugging stuff
#hi = where(mylsa.A )


