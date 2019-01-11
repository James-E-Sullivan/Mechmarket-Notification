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

    split_H = title.split('[H]')
    loc = split_H[0].strip(' ')
    split_W = split_H[1].split('[W]')
    haveString = split_W[0].strip(' ')
    wantString = split_W[1].strip(' ')

    print('Location:' + loc)
    print('Has: ' + haveString)
    print('Wants: ' + wantString)


    # Known issue. This return doesn't work.
    return titleList[loc, haveString, wantString]

# Test splitTitle with example text
splitTitle(new_title)
