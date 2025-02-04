s = {} # Empty dict
s = set() # Empty Set

# Unordered & Immutable & Unindexed
# In set 5 is different from '5' but 5 == 5.0
s = {1, 5, 53, 5, 1, "Anekant", "False", '5'} # Collection of well defined objects non - repetative


print(len(s)) 
print(s)

s.add("Jain") # Adds at the last
print(s)

print(s.remove(53)) # Removes the item
print(s)

s.pop() # Removes the random element
print(s)

# s.clear() # Empty set