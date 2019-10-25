import re
def emailmatch(email):
    regex = '^[(a-z)|(A-Z)|(0-9)|.-]+@(gmail.com|live.com|hotmail.com|yahoo.com)$'
    if(re.search(regex,email)):
        print ("Valid Email")
    else:
        print("Invalid Email")
        

##test cases        
emailmatch("a@gmail.com")
emailmatch("$@gmail.com")
emailmatch("ahmed@gmail.com")
emailmatch("_ahmed.arshed.562@gmaisdl.com")
emailmatch("a!@gmail.com")
emailmatch("1234@live.com")
emailmatch("@gmail.com")
emailmatch("ahmed@live.com")
emailmatch("$%#@gmail.com")
emailmatch("p176099@nu.edu.pk")
emailmatch("ahmed!arshed@hotmail.com")
emailmatch("waleed@gmail.c!om")
emailmatch("waleed.arshed.562@live.com")
emailmatch("ahmed.a@gmail.com")
emailmatch("a-arshed_a@gmail.com")