class ParentClass():
    def get_detail_of_parent(self):
        return f"I'm the parent class"

class ChildClass1():
    def get_detail_of_child1(self):
        return f"I'm the child class"

class ChildClass2(ParentClass, ChildClass1):
    def get_detail_of_child2(self):
        return f"I'm the child2 class"
    
    
child_cls_instance = ChildClass2()
print(child_cls_instance.get_detail_of_parent())

