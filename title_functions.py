new_title = '[US-MA] [H] TX-1800v2 [W] PayPal'
w = 'TX-1800'

#splitHave = s.split('[H]')
#splitWant = splitHave[1].split('[W]')
#output = splitWant[0]
#output = output.strip(" ")
#print(output)

#if w in output:
    #print('Your desired item is for sale.')

#else:
    #print('Try again later.')

def splitTitle(title):

    titleList = []

    if '[H]' in title and '[W]' in title:

        split_H = title.split('[H]')
        loc = split_H[0].strip(' ')
        split_W = split_H[1].split('[W]')
        haveString = split_W[0].strip(' ')
        wantString = split_W[1].strip(' ')

        #print('Location:' + loc)
        #print('Has: ' + haveString)
        #print('Wants: ' + wantString)

        titleList.append(loc)
        titleList.append(haveString)
        titleList.append(wantString)

        return titleList

    else:
        pass

# Test splitTitle with example text
#splitTitle(new_title)

#print(splitTitle(new_title))

def writeTitle(title):

    titleFile = open("textfile", "w")
    titleFile.write(title)
    titleFile.close()

def appendTitle(title):

    titleFile = open("textfile", "a")
    titleFile.write(title + "\n")
    titleFile.close()