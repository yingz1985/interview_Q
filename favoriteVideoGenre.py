def favoriteVideoGenre(numUsers, userBooksListenedTo, numGenres, bookGenres):
    #userGenresListened={}
    favorites = {}
    for entry in userBooksListenedTo:

        books = userBooksListenedTo[entry] #returns list of books
        #userGenresListened[entry]=[]

        CountGenres = {}
        for book in books:
            
            Max = 0
            for genre in bookGenres:
                CountGenres.setdefault(genre,0)
                if book in bookGenres[genre]:
                    print(entry,book,genre)
                    CountGenres[genre]+=1 #increment book count
                    if CountGenres[genre]>Max:
                        Max = CountGenres[genre] #keep count of the mode
                    break
            #print(CountGenres,Max)
            favorites[entry] = [x for x in CountGenres if CountGenres[x]==Max]
                    #userGenresListened[entry].append(genre)
    return favorites


userBooksListenedTo={
    'Fred':['m','w','s'],
    'Jenie':['h','p'],
    'Rone':['a']
    }
bookGenres ={
    'Horror':['m','s'],
    'Comedy':['h'],
    'Romance':['w','a','p']
    }


print(favoriteVideoGenre(3,userBooksListenedTo,3,bookGenres))

                
        
            
                

            
