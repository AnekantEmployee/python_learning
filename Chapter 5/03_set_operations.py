s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}

print(s1, s2)

print(s1.union(s2)) # Returns concat without repetation
print(s1.intersection(s2)) # Returns the common elements
print(s1 - s2) # Removes the items from the s1 which are in the s2
print(s1.issubset({2})) # This set exists or not