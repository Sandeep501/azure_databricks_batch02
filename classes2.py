# Employee Class

class employee:
    __bonus = 10000  # --> private variable
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def get_emp_details(self):
        return f"{self.name} belongs to employee class"
    
    def get_emp_salary(self):
        return f"{self.name} salary is: {self.salary}"
    
    def __get_sal_with_bonus(self):
        return f"{self.name} salary with bonus is: {self.salary + self.__bonus}"
    
    def get_sal_details(self):
        return self.__get_sal_with_bonus()


my_cls_ins = employee("Karthik", 20000)
print(my_cls_ins.get_sal_details())
# print(my_cls_ins.__bonus)


