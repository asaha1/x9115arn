class Employee(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return "Name = " + self.name + ", Age = " + str(self.age) + '\n'
        
    def __lt__(self, another):
        return self.age < another.age
        
one = Employee('Arnab', 25)
two = Employee('Abc', 50)
three = Employee('Def', 15)

print one
print two
print three

print one < two

list1 = [one, two, three]
list1.sort()
print list1