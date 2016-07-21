# Takes in two words and returns the edit distance 
def levenshtein_distance(first,second):
    
    columns = len(first) + 1
    rows = len(second) + 1
    
    current_row = [0]
    
    # Constructs first row 
    
    for column in xrange(1,columns):
        current_row.append( current_row[column - 1] + 1 ) 
    
    # The first column in the current row will 
    # be the cost of the first column in the previous row    
    for row in xrange(1,rows):
        previous_row = current_row
        current_row = [previous_row[0] + 1] 
    
    # The newest index in the current row will
    # be equal to the smallest value + 1 between
    # the previous index in the same row, 
    # the same row in the previous column
    # and the previous column in the previous row  
    # the edit distance will be the value in 
    # the last column of the last row 
        for column in xrange(1,columns):
            top_box = previous_row[column]
            left_box = current_row[column - 1]
            diagonal = previous_row[column - 1]
           
            if first[column - 1] != second[row - 1]:
                current_row.append(min(top_box,left_box,diagonal) +1) 
            else: 
                current_row.append(diagonal) 
                        
    return current_row[-1]
    
def fuzzymatch(input, gallery):
        # This dictionary will hold all the 
        # objects in the list input that
        # returns a successful search Then 
        # pair that object with the sorting
        # distance as its key
        dictionary = {}

        for column in gallery:
                search = input.lower()
                library = column.lower()

                # These variables control the iteration and loops below
                search_index = 0
                lib_index = 1

                # These here are to be used in the two step sorting process,
                # arranging our results in order of relevance
                distance_list = []
                edit_distance = 0
                sorting_distance = edit_distance

                for letter in library:

                        # This block of code may seem to be in repetition but
                        # is necessary so to return successful searches when the
                        # last character in the string is the last key to the
                        # search as well. This eliminates the false result that
                        # would be exhibited in that scenario
                        if lib_index >= len(library) and search_index == len(search) - 1 and library[len(library)-1] == search[len(search) -1]:
                                distance_list.append(library.index(letter))

                                # First step of the sorting process relying on
                                # the average distance between adjacent
                                # characters in the search input as observed
                                # in the list input
                                sorting_distance += (float(distance_list[-1] - distance_list[0])/(len(search)-1))

                                # first_word the users input 
                                # second_word the words in the list 
                                # both are passed as parameters into the 
                                # levenshtein distance function
                                # the function returns the edit distance
                                # the shortest number of edits required to 
                                # change second_word  into first_word
                                # note the function only considers the characters
                                # between the first appearence of the first 
                                # character in the input string 
                                # and the last character in the input string
                                # the edit distance will be used to sort the 
                                # objects in the list based on relevance
                                # smaller the edit distance number greater the relevance
                                first_word = search
                                second_word = library[distance_list[0] : distance_list[-1] + 1]
                                edit_distance += levenshtein_distance(first_word,second_word)
                                
                                sorting_distance += edit_distance
                                
                                #print(sorting_distance)

                                # This block of code first checks if a
                                # particular key has already been used. If so,
                                # then an object is append to the very same
                                # key.  If the more likely option of the key
                                # being not used as of yet, the object will be
                                # paired with the key
                                if dictionary.get(sorting_distance) != None :
                                    dictionary[sorting_distance].append(library)
                                else:
                                    dictionary[sorting_distance] = [library]
                                break

                        if search_index == len(search):

                            
                                # First step of the sorting process relying on
                                # the average distance between adjacent
                                # characters in the search input as observed
                                # in the list input
                                sorting_distance += (float(distance_list[-1] - distance_list[0])/(len(search)-1))

                                # first_word the users input 
                                # second_word the words in the list 
                                # both are passed as parameters into the 
                                # levenshtein distance function
                                # the function returns the edit distance
                                # the shortest number of edits required to 
                                # change second_word  into first_word
                                # note the function only considers the characters 
                                # between the first appearence of the 
                                # first character in the input string 
                                # and the last character in the input string
                                # the edit distance will be used to sort the 
                                # objects in the list based on relevance
                                # smaller the edit distance number greater the relevance
                                first_word = search
                                second_word = library[distance_list[0] : distance_list[-1] + 1]
                                edit_distance += levenshtein_distance(first_word,second_word)
                                
                                sorting_distance += edit_distance
                    
                                # This block of code first checks if a
                                # particular key has already been used. If so,
                                # then an object is append to the very same
                                # key.  If the more likely option of the key
                                # being not used as of yet, the object will be
                                # paired with the key
                                if dictionary.get(sorting_distance) != None :
                                    dictionary[sorting_distance].append(library)
                                else:
                                    dictionary[sorting_distance] = [library]
                                break

                        if lib_index >= len(library):
                            break

                        # This block of code here is the engine behind this
                        # operation. For more information visit the readme file
                        # or look up algorithm on fuzzy matching
                        if letter == search[search_index]:
                                distance_list.append(library.index(letter))

                                search_index += 1
                                lib_index += 1
                        else:
                            lib_index += 1
        # Final block of code to return objects in the list in order of
        # relevance in comparison to the search input by sorting the keys in
        # ascending order
        for key in sorted(dictionary):
            print dictionary[key]