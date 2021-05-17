
#Python fun with tags
#@Author Alexis Delgado
print "We're going to build a simple webpage together! Please follow the instruction below!"
outfile = open ("Hope.html", "w")
#This is the beginning of the Html document.
outfile.write( "<!DOCTYPE html>" + "\n<html>" + "\n<head>" + "\n</head>" + "\n<body>")
#First heading of the html document
outfile.write("\n<H1>" + raw_input("What would you like as your firt heading?: ") + "<\H1>" + "\n")
#prompt text for page.
outfile.write(raw_input("Please type the first message your visitors will see: "))
print
#prompt for the list heading.
outfile.write("\n<H2>" + raw_input("Please type the heading for your first list: ") + "</H2>")
isDone = False
alllistItem = ""
ordered = 0
listType = raw_input ("\nChoose order list (O) or undordered list (U): ")
#Initiation of loop for list type and appeneding itmes to list loop
while(listType == "O" or listType == "o"):   
    outfile.write("\n<ol>")
    ordered = 1
    if(ordered == 1 and isDone== False):
       listItem = raw_input("Enter an item (Type return when finished): ")
       outfile.write(alllistItem + ("\n<li>" + listItem + "</li>" ))
       if(listItem == "return" and ordered == 1):
           outfile.write("\n</ol>" + "\n</head>" + "\n</html>")
           outfile.close()
           isDone = True
           print "\nDone writing file - open with broswer"
if(listType == "U" or listType == "u"):
    outfile.write("\n<ul>")
    if(isDone == False and ordered == 0):
        listItem = raw_input("Enter an item (Type return when finished): ")
        outfile.write(alllistItem + ("\n<li>" + listItem + "</li>" ))
        if(listItem == "return"):
            outfile.write("\n</ul>" + "\n</head>" + "\n</html>")
            outfile.close()
            print "\nDone writing file - open with browser"
            isDone = True  

    
    
            
            
    

        
            
    



