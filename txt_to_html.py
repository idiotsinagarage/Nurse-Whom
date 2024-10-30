import os
#This program is meant to take 'Nurse Whom' formatted text files and convert them into html sites.
"""
THE FORMATTING FOR NURSE WHOM IS AS FOLLOWS:
-{TITLE OF EPISODE or NEXT EPISODE}-
{DESCRIPTION TEXT}
::LOCATION TEXT::
NAME: DIALOGUE [ACTION]
"""

#import the text file
filename = input("Input an valid file: ")
file = open(filename, "r")
lines = file.readlines()

#begin assembling the master string (this will be what is written to the html file)
mStr = "" #just putting in the basic formatting stuff

#now we go through every line of the array (each index is a full line of the document)
for i in range(0,len(lines)-1):
    #tabbing over
    mStr += "\t\t"
    #getting rid of new line character
    temp = lines[i][0:len(lines[i])-1]
    #now we have to go through each location and check the first character
    #if it isn't a special character ("-", "{}", or ":") we continue knowing it is dialogue.
    if len(temp) > 0:
        if temp[0] == "-":
            #turning the line into a title
            #wait okay I need to add the title to the begining.
            title = temp[3:-3].split(": ")
            mStr =  "\t\t<h2>--" + title[0] + "--</h2>\n" + mStr
            mStr += "<br>\n\t\t<br>\n\t\t<h1>NURSE WHOM:</h1>\n\t\t<h1>" + title[1] + "</h1>\n\t\t<br>\n\t\t<br>\n"
        elif temp[0] == "{":
            #turning the line into a description
            mStr += "<p><b><i>" + temp[1:-1] + "</i></b></p>\n"
        elif lines[i][0] == ":":
            #turning the line into a location
            mStr += "<h3><i>-" + temp[2:-2] + "-</i></h3>\n"
        else:
            #turning the line into dialogue
            tArr = temp.split(": ", 1)
            nm = tArr[0]
            if len(tArr) > 1:
                mStr += "<p><b>" + nm.upper() + ": </b>" + tArr[1] + "</p>\n"
            else:
                print("ERROR!!!!!!!!! (check result for location)")
                mStr += "ERROR!\n"
    else:
        mStr += "<br>\n"
mStr = "<!DOCTYPE html>\n<html>\n\t<head><title>NURSE WHOM - s1e" + filename.split(".")[0][18:] + "</title><link rel=\"stylesheet\" href=\"/Nurse-Whom/seasons/style-season.css\"></head>\n\t\t<body>\n" + mStr
next = lines[-1].split( ": ")[1][:-4]
nextInt = int(filename.split(".")[0][18:])+1
mStr += "<br>\n<br>\n<h2><a href=\"ep" + str(nextInt) + ".html\">--NEXT EPISODE: " + next + "--</a></h2>\n<h3><a href=\"ep" + str(nextInt-2) + ".html\">--PREVIOUS EPISODE: " + str(nextInt-2) + "--</a></h3>\n<br><br><br><p><a href=\"/Nurse-Whom/index.html\">HOME</a></p>\n<p><a href=\"/Nurse-Whom/seasons/season1.html\">SEASON ONE</a></p>\n"
mStr += "\t</body>\n</html>\n"
mStr = mStr.replace("(","<i>")
mStr = mStr.replace(")","</i>")
mStr = mStr.replace("[","<i>[")
mStr = mStr.replace("]","]</i>")
mStr = mStr.replace(" |"," <code>|")
mStr = mStr.replace("b>|","b><code>|")
mStr = mStr.replace("| ","|</code> ")
mStr = mStr.replace("|!","|</code>!")
mStr = mStr.replace("|.","|</code>.")
mStr = mStr.replace("|,","|</code>,")
writefile = filename[:-4]+".html"
if os.path.exists(writefile):
  os.remove(writefile)
wr = open(writefile, "w")
wr.write(mStr)
wr.close()