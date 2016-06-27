def fuzzymatch(input, gallery):
	dictionary = {}

	for column in gallery:
		search = input.lower()
		library = column.lower()
		search_index = 0
		lib_index = 1

		for letter in library:
			if lib_index >= len(library) and search_index == len(search) - 1 and library[len(library)-1] == search[len(search) -1]:
				if dictionary.get(lib_index) != None :
					dictionary[lib_index].append(library)
				else:
					dictionary[lib_index] = [library]
				break

			if search_index == len(search):
				if dictionary.get(lib_index) != None :
					dictionary[lib_index].append(library)
				else:
					dictionary[lib_index] = [library]
				break
							
			if lib_index >= len(library):
				break

			if letter == search[search_index]:
				search_index += 1
				lib_index += 1
			else:
				lib_index += 1 
	
	for key in sorted(dictionary):
		print dictionary[key]
