try:
    a = int(input("Hey, Enter the number: "))
    print(a)
except Exception as e:
    print(e)
finally:
    print("Thank You") # Works every time ## Even if the function returns it'll work
# else:
#     print("I am a else block") # Executes when try block is executed