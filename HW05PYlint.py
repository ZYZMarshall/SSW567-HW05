def plurals(string):
    wordlist = string.split()       # get all the word(s) from the string
     vowelslist = ('ay', 'ey', 'iy', 'oy', 'uy')
    endswithYlist = ('y')
     endswithElselist = ('o', 'ch', 's', 'sh', 'x', 'z')
    pluralstring = ''                # store the response in a string
    for words in wordlist:

         if words.endswith(vowelslist):             #use endwith() to check if words are end in vowelist

            pluralstring += words + 's' + ' '

        elif words.endswith(endswithYlist):       # end in endswithYlist

            pluralstring += words[:-1] + 'ies' + ' '

        e lif words.endswith(endswithElselist):   #end in endwithElselist

            pluralstring += words + 'es' + ' '

        else:

            pluralstring += words + 's' + ' '       #the normal end just add 's

        if words == wordlist[-1]:
            pluralstring = pluralstring[:-1]
    return pluralstring                                 #return the string after confirm the words in it are plural 


def getuserstring():
    username = input("Hello and welcome! What's your name? : ")
    userline = input('Hello! ' + username + ', please enter any statement or line : ')
    print('Prural of the line is : ', plurals(userline))


getuserstring()