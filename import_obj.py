from utils import (
    addition,
    greet,
    multiplication,
    sample_cls
)

print(greet())
print(addition(10, 20))
print(multiplication(10, 20))

s = sample_cls()
print(s.get_cls_details())

d = sample_cls()
print(d.get_cls_details())