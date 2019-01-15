#new_title = '[US-MA] [H] TX-1800v2 [W] PayPal'
#w = 'TX-1800'

def splitTitle(title):
    '''
    Precondition: title is a title of a submission from a post on /r/mechmarket

    Postcondition: return titleList, which is a list containing
    [Seller location, Seller's item for sale, Seller's wants]

    Notes:
    Sell/Buy posts on /r/mechmarket must be in the following format...
    [Location] [H] What the poster has [W] What the poster wants

    :param title:
    :return titleList:
    '''
    titleList = []


    if '[H]' in title and '[W]' in title:

        split_H = title.split('[H]')
        loc = split_H[0].strip(' ')
        split_W = split_H[1].split('[W]')
        haveString = split_W[0].strip(' ')
        wantString = split_W[1].strip(' ')

        titleList.append(loc)
        titleList.append(haveString)
        titleList.append(wantString)

        return titleList

    else:
        pass

def writeTitle(title):

    titleFile = open("title_file", "w")
    titleFile.write(title)
    titleFile.close()

def appendTitle(title):

    titleFile = open("title_file", "a")
    titleFile.write(title + "\n")
    titleFile.close()