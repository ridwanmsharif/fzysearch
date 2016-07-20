def fuzzymatch(input, gallery):
        # This dictionary will hold all the objects in the list input that
        # returns a successful search Then pair that object with the sorting
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
                levenshtein_distance = 0
                sorting_distance = levenshtein_distance

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
                                sorting_distance += (float(distance_list[-1] - distance_list[0])/(len(search_input)-1))

                                # Enter Levenshteins code here Ali and use
                                # these two words as input. Add comment here
                                # about the algorithm used
                                word_1 = search_input
                                word_2 = library[distance_list[0] : distance_list[-1]]

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
                                sorting_distance += (float(distance_list[-1] - distance_list[0])/(len(search_input)-1))

                                # Enter Levenshteins code here Ali and use
                                # these two words as input. Add comment here
                                # about the algorithm used
                                word_1 = search_input
                                word_2 = library[distance_list[0] : distance_list[-1]]

                                # This block of code first checks if a
                                # particular key has already been used. If so,
                                # then an object is append to the very same
                                # key. If the more likely option of the key
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
