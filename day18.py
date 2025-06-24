#Today I am learning something about Metaclass, it specify the rules for a class and how class need to be work. Metaclass is above the class that we are creating. 


class EnforceNaming(type):
    def __new__(self, class_name,bases,attrs):
        print(attrs)
        for name in attrs:
            if not name.islower():
                raise ValueError(f"Attribute {name} must be lower case!")
            
        return type(class_name,bases,attrs)

class myClass(metaclass = EnforceNaming):
    # my_var = 5
    MY_VAR = 5
    def new_func(self):
        print('hello')

new_class = myClass()
new_class.new_func()