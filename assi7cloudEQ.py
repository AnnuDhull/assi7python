#  Ques :   If we have an object which has both instance as well as class attr, who will get preference?
#  Ans :    Instance attribute will get the preference . 

class Animal :
     Dog = " Bark"
     cat ="meaooowww"
     frog = "croak"

     def __init__(home):
        home.Dog="kennel"

obj = Animal()
print(obj.Dog)

# ------------------------------------------------------------------------------------------------------------------------------

# Create a class and make three object with different parameters and change the values when you retrive data from the class 


class Friends :
    f1= ""
    f2= ""
    f3= ""

    def __init__(self, a , b , c ):

        self.f1=a
        self.f2=b
        self.f3=c
    def display(self):    
        print("f1 = "+ self.f1)
        print("f2 = "+ self.f2)
        print("f3 = "+ self.f3)
        print("----------------------------")

obj1 = Friends("Siddharth" , "Akansha " ,"Nikita")
obj2 = Friends("Komal" , "Dhruv" , "shivash")
obj3 = Friends("seema" , "shivani" ,"sunita")

obj1.display()
obj2.display()
obj3.display()

# ---------------------------------------------------------------------------------------------------------------------------------

#  Define Super method and Class method

#super method
# the method through which we can use the constructors ,attribute and methods of parent class.
#class methods
# these are inbuilt function in python ,these are bound to class rather than an object.