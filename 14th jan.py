##2
class Shape():
    def __init__(self,nameofShape):
        self.nameofShape = nameofShape

class Rectangle(Shape):
    def __init__(self, nameofShape, height, weidth):
        Shape.__init__(self,nameofShape)
        self.height = height
        self.weidth = weidth

    def GetArea(self):
        Area = self.height * self.weidth
        return Area

    def GetPerimeter(self):
        Perimeter = self.height + self.height + self.weidth + self.weidth
        return Perimeter


class Circle(Shape):
    def __init__(self, nameofShape, radius):
        Shape.__init__(self,nameofShape)
        self.radius = radius

def GetArea(self):
    Area = 3.14 * self.radius * self.radius
    return Area

def GetPerimeter(self):
    Perimeter = 2 * 3.14 * self.radius
    return Perimeter


##1
class Person:
    def __init__(self,name):
        self.__name = name

    def SetName(self,NewPerson):
        self.__name = NewPerson

    def GetPerson(self):
        return self.__name


class Contact(Person):
    def __init__(self,name,PhoneNumber,Address,Email):
        Person.__init__(self,name)
        self.__PhoneNumber = PhoneNumber
        self.__Address = Address
        self.__Email = Email

    def __del__(self):
        del self

    def GetPhoneNumber(self):
        return self.__PhoneNumber

    def SetPhoneNumber(NewPhoneNumber):
        __PhoneNumber = NewPhoneNumber

    def GetAddress(self):
        return self.__Address

    def SetAddress(NewAddress):
        __Address = NewAddress

    def GetEmail(self):
        return self.__Email

    def SetEmail(NewEmail):
        __Email = NewEmail


    def SaveToFile(self):
        file = open("Contact.txt","+a")
        file.write(self.__name, "-", self.__Email, "-", self.__PhoneNumber,'\n')

    def GetAllContact(self):
        lines = []
        with open("Contacts.txt") as temp:
            for line in temp:
                lines.append(line)
        print(lines)


    def GetContactFromFile(self,name):
        lines = []
        with open("Contacts.txt") as temp:
            for line in temp:
                lines.append(line)
        filteredList= []
        for line in lines:
            t= line.split('-')[0]
            if(t==name):
                filteredList.append(line)
        return filteredList

