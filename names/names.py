from bst import BSTNode

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
'''
Replace the nested for loops below with your improvements
ORIGINAL RUNTIME: 6.304232835769653 seconds
ORIGINAL RUNTIME COMPLEXITY: O(n^2)
'''
#
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

'''
Implementation with a Binary Search Tree
NEW RUNTIME: 0.09333682060241699 seconds
NEW RUNTIME COMPLEXITY: O(n log n)?
'''
xer = BSTNode('Matt')
for name in names_1:
    xer.insert(name)

for name in names_2:
    if xer.contains(name):
        duplicates.append(name)

'''
Implementation using sets (Stretch)
NEW RUNTIME: 0.0048961639404296875 seconds
NEW RUNTIME COMPLEXITY: O(n) --> O(1)
'''

# dup_names = set(names_1).intersection(set(names_2))
# duplicates = list(dup_names)

'''
Implementation with a list search function
NEW RUNTIME: 0.37038707733154297 seconds
NEW RUNTIME COMPLEXITY: O(n log n)?
'''
# names_1.sort()


# def dup_search(arr, targ=None):
#     mid_ind = len(arr) // 2
#     if targ != arr[mid_ind] and len(arr) == 1:
#         return False
#     if targ == arr[mid_ind]:
#         return True
#     elif targ > arr[mid_ind]:
#         return dup_search(arr[mid_ind:], targ)
#     elif targ < arr[mid_ind]:
#         return dup_search(arr[:mid_ind], targ)


# for name in names_2:
#     res = dup_search(names_1, name)
#     if res:
#         duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
'''
See solution above using sets (lines 46 and 47)
'''
