#polymorphism
#method overraiding/runtime polymorphism
"""
we need multiple classes with inheritance--> carry on same functions
"""

class phone:
    def fun1(self):
        print("Talk with friends...")

class smart_phone(phone):
    def fun1(self):
        super().fun1()
        print("Talk and chat with your friends..")


# sm = smart_phone()
# sm.fun1()


#Abstraction in python
"""
abc -> abstract base class module
ABC -> abstract base class
abstrcatmethod --> function
"""
from abc import ABC,abstractmethod
class ebook(ABC):#abstract class
    @abstractmethod
    def source(self):
        print("Book Name : Learn Python")
        print("Author Name : Pradeepa")
        print("Sensitive data")
    def java_source(self):
        print("Book Name : Learn java")
        print("Author Name : praveen")
        print("Sensitive data")

class vendor(ebook):
    def source(self):
        print("Book Name : Learn Python")
        print("Author Name : Naga raj")

# v = vendor()
# v.source()
# v.java_source()

#encapsulation
"""
we archive the using access modifier
private => (__) => that property only access from inside class
protected => (_) => that property aceces own class  and child class 
public => that can be access any where and any one
"""
class ac_details:
    name = "Praveen Kumar"
    _ac_no = 123456786
    __pin = None
    def setPin(self,p):
        self.__pin = p
    def getName(self):
        return self.name
class bank(ac_details):
    _ac_no = 876543225
    def fun1(self):
        print(self.name)
        # print(self.__pin)
# ac = ac_details()
# print(ac.name)
# print(ac.__pin)
b = bank()
b.fun1()
b.setPin(3456)

name = b.getName()
print("AC Holder Name :",name)








































