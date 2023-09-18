#Create a class named FirstClass and two classes named SecondClass and ThirdClass that inherits from FirstClass.
# Create class named FourthClass that inherits from Second and Third. Create a common method called testMethod in all the classes and
# provide the Method Resolution Order for the given hierarchy
class FirstClass:
    def testMethod(self):
        print("FirstClass testMethod")

class SecondClass(FirstClass):
    def testMethod(self):
        print("SecondClass testMethod")

class ThirdClass(FirstClass):
    def testMethod(self):
        print("ThirdClass testMethod")

class FourthClass(SecondClass, ThirdClass):
    pass

# Method Resolution Order (MRO)
print("Method Resolution Order:", FourthClass.mro())
first_instance = FirstClass()
second_instance = SecondClass()
third_instance = ThirdClass()
fourth_instance = FourthClass()

first_instance.testMethod()
second_instance.testMethod()
third_instance.testMethod()
fourth_instance.testMethod()
