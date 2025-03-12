# class first_class:
#     pass

param1 = 12
param2 = 23

class calculator:
    def __init__(self):
        # self.num1 = num1
        # self.num2 = num2
        pass
        
    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mul(self, num1, num2):
        return num1 * num2
    
    def div(self, num1, num2):
        return num1 // num2
  
    
first_instance = calculator()
print(first_instance.add(10, 30))
print(first_instance.mul(1, 30))