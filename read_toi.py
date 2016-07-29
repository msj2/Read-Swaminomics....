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
lul = full_url
print lul
content = lxml.html.parse(full_url)

# Doesn't work: Is div class = content under div id = sform2...... Try///
# Prints empty..
#lines = content.xpath("//div/@sform2")

lines = content.xpath("//p/text()")		# Sexy Works.. But gets only Text, not the URL...
#lines = content.xpath("//a/@href") # Works
#lines = content.xpath("//img/@src") # Works



##import lxml.html

##htmltree = lxml.html.parse('http://www.google.com/intl/en/about/corporate/index.html')

##p_tags = htmltree.xpath('//p')
##p_content = [p.text_content() for p in p_tags]

##print p_content



#http://stackoverflow.com/questions/8226490/finding-html-element-with-class-using-lxml
#	Doesn't work, Prints the below
#lines = content.xpath("//div[contains(@class, 'content')]")
#<Element div at 0x7fdb9c8b83c0>
#<Element div at 0x7fdb9c8b8418>
#<Element div at 0x7fdb9c8b8470>
#<Element div at 0x7fdb9c8b84c8>


#Doesn't work, Prints the below
#<Element div at 0x7f863aa8c3c0>
#lines = content.xpath("//div[@class='content']")
for each in lines:
	print each

end=datetime.now()
time_taken = end - start
print "Time taken = ", time_taken
