class Employee:
    name = "Anekant"
    salary = 14780
    
    def __init__(self, name):
        self.name = name
        
    def getInfo(self):
        print(f'My name is {self.name} and salary is {self.salary}')
    
anekant = Employee("Anekant")
shiv = Employee("Shiv")
anekant.getInfo() # Employee.getInfo(anekant)
shiv.getInfo() 