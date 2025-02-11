f = open("file.txt", 'r')
f1 = open("file.txt", 'r')
data = f.read()
lines = f1.readlines()
print(lines)
print(data)
f.close()

f = open("my_file.txt", 'w')
f.write("Hello world")
f.close()

f = open("my_file.txt", 'a')
f.write("\nMy updated file name is Anekant")
f.close()

# + : Open for updating
# rb : Open in binary mode
# rt: default read text

with open('file.txt') as f:
    print("\nWith open file")
    print(f.read())