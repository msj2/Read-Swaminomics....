'''
this doesn't work for swarajyamag.com.... 
'''
#http://blogs.timesofindia.indiatimes.com/Swaminomics/do-not-misuse-lokpal-act-to-harass-ngos/

#	Try reading above page....

#<div class="content"> This tag contains Swami's text'

from datetime import datetime
import lxml.html
from sys import argv
start=datetime.now()
#full_url = raw_input("URL enter maadi: ")
full_url = argv[1]
#full_url = "http://blogs.timesofindia.indiatimes.com/Swaminomics/do-not-misuse-lokpal-act-to-harass-ngos/"

content = lxml.html.parse(full_url)


lines = content.xpath("//p/text()")		#  Works.. But gets only Text, not the URL.

for each in lines:
	print each

end=datetime.now()
time_taken = end - start
print "Time taken = ", time_taken, "Now, you gotta read it within 5 min & take Altraday tablets"
