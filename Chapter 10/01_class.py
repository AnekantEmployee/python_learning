class Employee:
    name = "Anekant"
    salary = 14780
    
    # Constructor
    def __init__(self, name):
        self.name = name
        
    def getInfo(self):
        print(f'My name is {self.name} and salary is {self.salary}')
    
    @staticmethod # If we don't want self method
    def goodMorning():
        print("Good morning")
    
anekant = Employee("Anekant")
shiv = Employee("Shiv")
anekant.getInfo() # Employee.getInfo(anekant)
shiv.getInfo()

# Printing static data
anekant.goodMorning() 