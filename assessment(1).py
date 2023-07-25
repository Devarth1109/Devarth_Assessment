class Student:
    def display(self):
        print("select your choice")

class Student1(Student):
    def display1(self):
        print("for councelor {press 1)")
        print("for faculty (press 2)")
        print("for student (press 3)")

class Student2(Student1):
    def display2(self):
        role = input("enter your role id: ")
        if role == "1":
            print("add student (press 1)")
            print("remove student (press 2)")
            print("view all student (press 3)")
            print("view specific studnet {press 4)")
        else:
            print("invalid number")

class Student3(Student2):
    def display3(self):
        choice = input("Enter your role id: ")
        d1={}
        f1={}
        l1={}
        c1={}
        s1={}
        m1={}
        fe1={}
        s2={}
        m2={}
        fe2={}
        if choice == "1":
            sr = int(input("Enter serial number: "))
            d1['sr']=sr
            fname = input("Enter a first name : ")
            f1['fname']=fname
            d1['fname']=f1
            lname = input("Enter a last name: ")
            l1['lname']=lname
            d1['lname']=l1
            contact = int(input("Enter a contact number: "))
            c1['contact']=contact
            d1['contact']=c1
            sub1 = input("Enter a subject: ")
            s1['sub1']=sub1
            d1['sub1']=s1
            mark1 = input("Enter a marks: ")
            m1['mark1']=mark1
            d1['mark1']=m1
            fees1 = input("Enter a fees: ")
            fe1['fees1']=fees1
            d1['fees1']=fe1
            sub2 = input("Enter a subject: ")
            s2['sub2']=sub2
            d1['sub2']=s2
            mark2 = input("Enter a marks :")
            m2['mark2']=mark2
            d1['mark2']=m2
            fees2 = input("Enter a fees: ")
            fe2['fees2']=fees2
            d1['fees2']=fe2
            print(d1)
        else:
            print("Your chouce is wrong")

class Student4(Student3):
    def display4(self):
        operation = input("Faculty want to perform any other operations? (Y/N)")
        if operation == "Y":
           print("Add marks to student (press 1)")
           print("view all student (press 2)")
        else:
            print("Thankyou...")

class Student5(Student4):
    def display5(self):
        choice1=input("Enter a choice by faculty: ")
        

s5 = Student5()
s5.display()
s5.display1()
s5.display2()
s5.display3()
s5.display4()
s5.display5()
