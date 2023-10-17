# In this exersice we will find an element in the list the most efficient way as possible.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# First thing we do, is to cut the list into two halves.
# Check again after we cut the list in half, is the number in the first half or the second?
# After finding the number in one of the halves, we cut the other half into two halves to check in what half the element located
# Again, cut the final list into two halves. We will keep doing that until we get only the element we want to find,
# this way we will end up with the element without looping over entire list.
