class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @staticmethod  # Method that doesn't need self
    def company_policy():
        return "Follow company rules."
    
    @property  # Getter for name for encapsulation
    def name(self):
        return self._name
    
    @name.setter  # Setter for name
    def name(self, new_name):
        self._name = new_name
    
    @property  # Getter for salary
    def salary(self):
        return self._salary
    
    @salary.setter  # Setter for salary
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
    
    @classmethod  # Works with class, not instance
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))
    
# Usage
emp = Employee("Anekant", 50000)
print(emp.name)  # Uses @property getter
emp.name = "Shiv"  # Uses @name.setter
print(emp.salary)
emp.salary = 60000  # Uses @salary.setter
print(Employee.company_policy())  # Calls @staticmethod
new_emp = Employee.from_string("John-40000")  # Uses @classmethod
print(new_emp.name, new_emp.salary)
