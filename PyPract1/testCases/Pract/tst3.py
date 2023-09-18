class InterviewbitEmployee:
    # protected members
    _emp_name = None
    _age = None
    __branch = None
    def __init__(self, emp_name, age, branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch
    def display(self):
        print(self._emp_name + " " + self._age + " " + self.__branch)
l1=InterviewbitEmployee('srikanrht',34,'ece')
print(l1._emp_name)
print(l1._age)
# print(l1.__branch)