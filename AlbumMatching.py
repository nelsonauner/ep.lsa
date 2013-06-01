#By: Aniket Karmarkar
#Date: 8/31/2012
#Description: The following file takes two strings and prints the levenstein distance and converts it to a percentage.

from __future__ import division
import nltk


albumOld ="hello"
albumNew ="yellow"

levenshtein_distance = nltk.metrics.distance.edit_distance(albumOld, albumNew)
maximum_string_length = len(max(albumOld, albumNew))
print((1.0 - (levenshtein_distance/maximum_string_length))* 100)
    
