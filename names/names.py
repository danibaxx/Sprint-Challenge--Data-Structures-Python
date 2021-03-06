import time
import os
import sys

start_time = time.time()

with open(os.path.join(sys.path[0], 'names_1.txt'), 'r') as f:
# f = open('names_1.txt', 'r')
  names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()
with open(os.path.join(sys.path[0], 'names_2.txt'), 'r') as f:
# f = open('names_2.txt', 'r')
  names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
            # O(n^2)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        found = False
        if self.value >= target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        if self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

names = BSTNode('John')

for name in names_1:
  names.insert(name)

for name in names_2:
  if names.contains(name):
    duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
