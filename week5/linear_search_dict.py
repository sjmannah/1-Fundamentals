def linear_search_dictionary(dictionary, target):

    for x in dictionary:
        #print(dictionary[x])
        if dictionary[x] == target:
            print("Found at index", x)
            return 
    
    print("Target is not in the list")

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)

