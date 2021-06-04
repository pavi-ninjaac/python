class employee:
    __emp_global = 100
    a = 10
    def __init__(self,name , salary):
        self._name = name
        self.__salary = salary
    
    def getsalary(self):
        return self._name

    def getsalary(self):
        print("aceessing the private value by the method")
        return self.__salary
    def get_global(self):
        print("getting the global a",self.__class__.a)
        print(self.__class__._employee__emp_global)


print(employee.__dict__)
e = employee('pavi' , 10000)
print(dir(e))
print(e._name)
print(e.getsalary())
print("accessing the private value-->salary")
print(e._employee__salary)
print(e.getsalary())
e.get_global()
