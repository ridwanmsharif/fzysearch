Fzysearch Engine

Operates in accordance to the principal of Fuzzy Matching.
Iterates through a list of objects (Preferably of data type string), comparing 
each object to the search input. Successful matches result in the object being 
placed in a dictionary aside its unique corresponding sorting variable as its key.

Principle Of Fuzzy Matching

The engine pits each object in the list against the searched string and breaks 
each down for a character specific comparison. If the object completes the criteria 
of a successful search, it can be paired with a key and then inserted into the 
dictionary. For a successful search, ALL of the following must be true for the given 
object: 
It must contain equal or more number of characters than that of the searched string.
It must contain every character in the searched string (Including spaces and special 
characters) The characters in the searched input must appear in the very same 
succession in the object (Other characters/letters may come in between as long as 
all letters are present in the right order)
It does so using the following block of code:
if letter == search[search_index]:
	search_index += 1
        lib_index += 1
else:
	lib_index += 1

Lib_index and search index act as the parameter and so control the search process.
Then loops and if statements are used to break results out and return them when
triggered.

Dictionary

This feature of the engine is responsible for the sorting, returning and displaying 
of the successful results on completion of the loop. It does so by pairing the 
successfully matched object with a unique sorting variable (data type float) as its key.
The sorting variable is assigned to the object if and only when the object breaks out 
of the iteration successfully. The dictionary is later sorted in ascending order of 
the keys thus returning objects in order of relevance.

Sorting Variable

This variable (data type float) is responsible for the order or relevance of the results. 
It is calculated using a two step system. The value is a weighed average of Levenshtein's 
Edit Distance and the mean distance between relevant characters in the object 
(average distance between successive characters in the search as it appears in the object)
The weight of each step to be determined. For now both are given equal footing. The average 
distance is calculated arithmetically inside the loop, whereas the Edit distance is 
calculated by calling a predefined function we've written.
The first input to the Levenshtein's predefined function is the searched string. the second
however poses a problem. So to avoid discrepancies and higher values because of object length, 
I've chosen to use only a part of the object (Using the extreme poles of the search string) 
for the second input.
I've found that this works perfectly as this step is only carried out if and only when the 
object is successfully matched.
Additional steps can and will be added to improve on this at a later date. 

