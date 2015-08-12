# -*- coding: utf8 -*-

"""
This program reads a Thomson Reuters Web of Science(TM) file
and creates a wordcloud for articles published
It should work with any file following the ISI format.
"""

from sys import argv
import numpy as np
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Printing an error message in case the user forgets filename.
print '-' * 10
print 'USAGE: python WOSkeywordcloud.py filename'
print '_' * 10

# Opening and reading the file selected by the user.
script, filename = argv
f = open(filename)
wosrecords = f.read()

text = []

# Counts the articles in the dataset.
# Number of articles (PT) should match what you downloaded from WoS.
def articlecount():
    result = re.findall(r'^PT', wosrecords, flags = re.MULTILINE)
    articles = len(result)
    return articles

# Defining the regular expression to extract the DE field (keywords).
def findkeywords():
    result = re.findall(r'^DE(.*)', wosrecords, flags = re.MULTILINE)
    text.append(result)

findkeywords()

# Converting the "text" list above to one single string.
for t in text:
    textstring = ''.join(t)
    print textstring

# Printing a message for the impatient user. 
print '-' * 10
print 'Creating wordcloud from %s articles (this may take some time)...' % articlecount()
print '-' * 10

# Generating wordcloud
wordcloud = WordCloud(
        background_color="white", 
        max_words=2000, 
        stopwords=STOPWORDS,
        width=2000,
        height=1000
        )
wordcloud.generate(textstring)

# Generating the image and showing it.  
plt.imshow(wordcloud)
plt.axis("off")
print 'Saving as wordcloud.png...\n Please close the window to return to terminal.'
plt.savefig("wordcloud.png") # change to .svg, .pdf etc. for other outputs. 
plt.show()
