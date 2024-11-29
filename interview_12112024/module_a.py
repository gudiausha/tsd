#how do u solve circular imports
# E:\practise>python module_a.py
# Traceback (most recent call last):
#   File "E:\practise\module_a.py", line 1, in <module>
#     from module_b import func_b
#   File "E:\practise\module_b.py", line 1, in <module>
#     from module_a import func_a
#   File "E:\practise\module_a.py", line 1, in <module>
#     from module_b import func_b
# ImportError: cannot import name 'func_b' from partially initialized module 'module_b' (most likely due to a circular import) (E:\practise\module_b.py)

from module_b import func_b
 
def func_a():
    print("Function A in module A")
    func_b()

from module_a import func_a
 
def func_b():
    print("Function B in module B")
    func_a()