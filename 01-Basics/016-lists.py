# my_list = [1,2,3] # Assign a list to a variable named my_list

# my_list = ['A String', 23, 100.233, 'o'] # Lists can hold different object types

# list_length = len(my_list) # List length

###### Indexing and Slicing

# my_list = ['one','two','three',4,5]

# list = my_list[0] # Grab element at index 0

# list = my_list[1:] # Grab index 1 and everything past it

# list = my_list[:3] # Grab everything UP TO index 3

# concatenate = my_list + ['new Item'] # Concatenate in list but this does not actually change the original list

# my_list = my_list + ['Add new Item'] # Reassign the list to make the change permanent

# my_list = my_list * 2 # We can also use * for duplication method similar to strings


###### Basic List Methods

# l = [1,2,3] # Create a new List

# l.append('New Item') # Append new item in list

# l.pop() # Pop for pop off an item from the list. By default pop takes off the last index, but you can also specify which index to pop off

# l.pop(1) # Pop off the 1 indexed item

# new_list = ['a','e','x','b','c']

# new_list.reverse() # Use reverse method to reverse order (This is permanent)

# new_list.sort() # Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)

# num_list = [1,3,6,7,4,2,8,9,] # Create list of descending order

# num_list.sort() # In this case sort use to sort list in Acceding order


###### Nesting lists

# Lets make three lists
lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]

matrix = [ lst_1, lst_2, lst_3 ] # Make a list of Lists form of matrix
# matrix = matrix[0][0] # Grab the first item in Matrix object

first_col = [ row[0] for row in matrix ] # Build a list comprehension by deconstructing a for Loop within a []

print(  first_col )