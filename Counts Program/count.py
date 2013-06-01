# 
# count.py
# 
# Input : full text filename
# Output: table file
# Desc  : Counts the number of occurrences of each term in all lyric files
#
# Written for Prof. Elizabeth Pontikes
# 
# References:
# http://mysql-python.sourceforge.net/MySQLdb.html#mysqldb
# http://www.kitebird.com/articles/pydbapi.html
# http://docs.python.org/howto/regex.html
# 


# Notes:
# Make sure all .txt files are in the local directory
# (terms file eg. kbbcars.txt, lyric location file ie. files_with_years_032611.txt, and lyric files eg. /anonymous/...)



# 0.
# Import libs
# -----------
import sys
import re	# regex


# 1.
# Connect to db
# -------------
'''import MySQLdb
dbdata	= {
	'host':'gsbhrdb01.chicagobooth.edu',
	'user':'lyrics',
	'pswd':'q1M@B3ll1',
	'dtbs':'HipHop' }
try:
	db	= MySQLdb.connect(
		dbdata['host'],
		dbdata['user'],
		dbdata['pswd'],
		dbdata['dtbs'] );
except MySQLdb.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)'''


# 2.
# Get list of terms from text file
# --------------------------------
file0	= raw_input("Enter full text filename: ")
FILE	= open(file0, 'r')
terms	= FILE.readlines()
terms	= [term.split('||') for term in terms]	# Parse with || delimiter
terms	= [term for sublist in terms for term in sublist]	# Flatten nested lists
terms	= [term.strip() for term in terms]	# Remove whitespaces
terms	= [term.lower() for term in terms]	# Convert to lowercase
FILE.close()


# 3.
# Get list of each track lyric text files
# ---------------------------------------
#  This is every file with an album id - must be updated with new album ids.
#  This just points you to the list of files.
file	= 'SourcePath.txt'
FILE	= open(file, 'r')
tracks	= FILE.readlines()
tracks	= [track.split(',,,') for track in tracks]	# Parse with ,,, delimiter
tracks	= [track for sublist in tracks for track in sublist]	# Flatten nested lists
tracks	= [track.strip() for track in tracks]	# Remove whitespaces
FILE.close()


# 4.
# Create table file for writing
# -----------------------------
file	= file0.split('.')
file	= file[0] + '_counts'
OUT 	= open(file, 'w')


# 5.
# Set up table headers with \t delimiters
# ---------------------------------------
# print terms
OUT.write('ArtistID')
OUT.write('\t')
OUT.write('Artist')
OUT.write('\t')
OUT.write('AlbumID')
OUT.write('\t')
OUT.write('Album')
OUT.write('\t')
OUT.write('Track')
for term in terms:
	OUT.write('\t')	
	OUT.write(term)
OUT.write('\t')
OUT.write('Link')
OUT.write('\r\n')	# New line


# 6.
# Search through each track lyric for terms
# -----------------------------------------
tracks	= ['lyrics1.txt','lyrics2.txt'] # test files
for track in tracks:
	# a. Get track data
	FILE	= open(track, 'r')
	lines	= FILE.readlines()
	FILE.close()
	# b. Store metadata
	artist	= lines[0].strip()
	album	= lines[1].strip()
	song	= lines[2].strip()
	# c. Initialize term counts
	counts	= {}
	# d. Find all term occurrences in each line
	for term in terms:
		for line in lines:
			matches = re.findall('[\W]*'+term+'[e]*[s]*[\W]', line, re.IGNORECASE)
			if len(matches) > 0:
				if term in counts:
					counts[term] = counts[term] + len(matches)
				else:
					counts[term] = len(matches)
	# e. Output to table if occurrences found
	match = 0
	if len(counts.keys()) > 0:
		match = 1
	if match == 1:
		OUT.write('1234')
		OUT.write('\t')
		OUT.write(artist)
		OUT.write('\t')
		OUT.write('5678')
		OUT.write('\t')
		OUT.write(album)
		OUT.write('\t')
		OUT.write(song)
		OUT.write('\t')
		for term in terms:
			if term in counts:
				num = str(counts[term])
			else:
				num = 0
				num = str(num)
			OUT.write(num)
			OUT.write('\t')
		OUT.write(track)
		OUT.write('\r\n')


# 7.
# Close output file
# -----------------
OUT.close()

