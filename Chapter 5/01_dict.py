a = {
    "Anekant": 100,
    "ABCD": 51,
    "Harry": 80
}
# Unordered Mutable datatype that data can be changed

print(a)
print(len(a))
print(type(a))
print(a.keys()) # Returns a list
print(a.values()) # Returns a list
print(a.items()) # Returns a list of tuple of key value pairs

print(a['Anekant']) # O(1) time because of indexing 
print(a.get('Anekant')) # Won't throw any error


a['Anekant'] = 99 # Updates original
print(a)

a.update({"Anekant": 90, "Renuka": 85}) # Update and add both at the same time
print(a)

print(a.pop('Harry')) # Removes the item
print(a)

print(a.popitem()) # Removes the last item
print(a)
