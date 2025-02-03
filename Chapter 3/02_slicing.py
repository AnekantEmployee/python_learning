# Slicing
str = 'Anekant'
print(str[:])
print("Length is ", len(str))
print(str[:1]) # Excludes the last
print(str[2:])

print("")
# print('Negative Slicing')
# Just start counting from the end
print(str[:-1])
print(str[-5:])

print("")
# Third Key
# print("Skip Value")
# print(str[0:7:0]) # Not possible
print(str[0:7:1])  # Default skip
print(str[0:7:2]) # One value skip

# Reverse the string
print(str[::-1])