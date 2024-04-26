
strText1 = """In publishing and graphic design, Lorem george.smith@google.com ipsum
is a placeholder text commonly used to demonstrate the visual form of a document or
a typeface without relying on george.smith@google.com meaningful content. Lorem
henry@yahoo.com ipsum may be used as a placeholder before final copy is available.
It is also used to temporarily (test@gmail.com) replace text in a process called
greeking, which allows designers to consider the form of a webpage or
newmail@hotmail.com. publication, without the meaning of the text influencing the
design."""
strText2 = """The Internet (or internet)[a] is the global@gmail.com system of
interconnected computer networks that uses the Internet protocol suite (TCP/IP)
[dave@hotmail.com] to communicate between networks and devices. It is a network of
networks that consists of private, public, academic, business, and government
networks of local to global scope, linked by a broad array of electronic, wireless,
and optical networking technologies. The Internet carries a vast range of
bill@network.us information resources and services, such as the inter-linked
hypertext@linkedin.org documents and applications of the World Wide Web (WWW),
electronic mail, telephony, and file sharing."""
listEmail = ["bill@network.us","george.smith@google.com", "test@gmail.com"]

# Do this assignment WITHOUT the global keyword
# Function that takes in a string, and returns a list of emails found.
def findEmails(strText):
    lisEmails = []
    lisText = strText.split()
    for strWord in lisText:
        if str(strWord).find("@") != -1:
            # Function to clean emails
            strCleaned = cleanEmail(strWord)
            lisEmails.append(strCleaned)
    return lisEmails

def cleanEmail(strText):
    arEmail = strText.split("@")
    strFront = arEmail[0]
    strBack = arEmail[1]
    strFront = strFront[::-1]
    # Function to return only good char.
    strBack = goodChar(strBack)
    strFront = goodChar(strFront)

    strFront = strFront[::-1]
    strClean = strFront + "@" + strBack
    return strClean

def goodChar(strText):
    strGood = ""
    if strText[-1:].isalnum() == False:
        strText = strText [:-1]

    for strChar in strText:
         if strChar.isalnum() == True or strChar == "." or strChar == "_" or strChar == "-":
            strGood += strChar
         else:
             break
    return strGood

lisEm1 = findEmails(strText1)
lisEm2 = findEmails(strText2)
# print(lisEm2)
lisEm1.extend(lisEm2)
print(lisEm1)

# Function that removes duplicates in a list, taking a list as input and returning
# the list without duplicates.m
def removeDup(lisEmails):
    lisNoDup = []
    for strEmail in lisEmails:
        booFound = False
        for strNewEmail in lisNoDup:
            if strEmail == strNewEmail:
                booFound = True
                break  # Break here to avoid unnecessary iterations
        if booFound == False:
            lisNoDup.append(strEmail)
    return lisNoDup

print(removeDup(lisEm1))

# Function that takes a string and a list as input and returns a True or False
# depending on whether the string value is in the list or no


def isInList(strEmail, lisEmails):
    return strEmail in lisEmails