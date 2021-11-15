'''
*********
PROGRAM 3
*********
Define a function second_smallest that takes a list of integers or floats as an argument. The function returns the 2nd smallest number in the list.
'''
def second_smallest(lst):
  lst.sort() #for descending, it would be lst.sort(reverse=False)
  return lst[1]
