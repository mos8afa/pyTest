#                                                   map()
#Purpose: Applies a function to each item in a sequence and returns a new sequence with the transformed items.
#Inputs: A function + an iterable (like a list).
#Output: A new iterable (like a list) where each element is the result of the function applied to the original element.
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]
#---------------------------------------------------------------------------------------------------------------------------
#                                                 filter()
#Purpose: Filters elements from a sequence using a condition.
#Inputs: A function that returns True or False + an iterable.
#Output: A new iterable containing only the elements that satisfy the condition.
numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]
#---------------------------------------------------------------------------------------------------------------------------
#                                                  reduce() 
#Purpose: Reduces a sequence to a single value by repeatedly applying a function to pairs of elements.
#Inputs: A function + an iterable.
#Output: A single result, like a total or product.
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 10
#---------------------------------------------------------------------------------------------------------------------------
