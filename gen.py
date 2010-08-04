#!/usr/bin/python

import sys, os, re
from xml.dom.minidom import Document	

tables=[]
errors=[]
ingroup = False
currenttable = ''


xmlDoc = Document()

pi= xmlDoc.createProcessingInstruction("xml-stylesheet","type=\"text/xsl\" href=\"template.xsl\"")
xmlDoc.insertBefore(pi, xmlDoc.documentElement)

wml = xmlDoc.createElement("database")
xmlDoc.appendChild(wml)

schema = open(sys.argv[1], 'r')
result = file(sys.argv[2],"w")


createTablePattern = re.compile(r'^\s+create_table \"([a-z_-]+)\"',re.M|re.I)
endTablePattern = re.compile(r'^\s+end',re.M|re.I)
fieldPattern = re.compile(r'^\s+t\.[a-z]+\s+\"([a-z0-9-_]+)\"',re.M|re.I)



for i, line in enumerate(schema):
	if re.match('^\s+$',line,re.M|re.I):
		continue
	if not ingroup:
		match = createTablePattern.match(line)
		if match:
			ingroup = True
			currenttable = match.group(1)
			maincard = xmlDoc.createElement("table")
			maincard.setAttribute("name", currenttable)
			wml.appendChild(maincard)
#			print currenttable
			continue
	else:
		match = fieldPattern.match(line)
		if match:
#			print currenttable,' => ',match.group(1)
			secondcard = xmlDoc.createElement("field")
			secondcard.setAttribute("name", match.group(1))
			maincard.appendChild(secondcard)
			continue
		match = endTablePattern.match(line)
		if match:
			ingroup = False
			continue
	errors.append(line)


#add verbose option for errors. to print only if wanted	
#print "---- ERRORS ----"
#for item in errors:
#	print item.strip()
	
result.write(xmlDoc.toprettyxml(indent="  ",encoding="ISO-8859-1"))


