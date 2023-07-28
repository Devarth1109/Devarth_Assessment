def main_menu():
    m = '''
        press 1 for counselor
        press 2 for faculty
        press 3 for student
        
    '''
    print(m)

    choice = input("Enter choice from above: ")
    if choice == '1':
        sm = '''
            1. add stu
            2. remove stu
            3. view all
            4. view specific stu
            '''
        print(sm)
        op=input("select option from above : ")
        stu_no=int(input("how many students you want to add : "))
        stu_dic={}
        stu_info={}
        sub={}
        m_f={}
        for i in range(1,stu_no+1):
            if op=='1':
                sno=int(input("Enter sr no : "))
                fname=input("Enter fname : ")
                lname=input("Enter lname : ")
                contact=input("contact : ")
                subject=input('Enter sub : ')
                marks=int(input('marks : '))
                fees=int(input("fees : "))
                subject1=input('Enter sub : ')
                marks1=int(input('marks : '))
                fees1=int(input("fees : "))
                fac=input("Enter fac name : ")

                m_f['marks']=marks
                m_f['fees']=fees
                m_f['marks1']=marks1
                m_f['fees1']=fees1
                sub[subject]=m_f
                sub[subject1]=m_f
                stu_info['fname']=fname
                stu_info['lname']=lname
                stu_info['contact']=contact
                stu_info['subject']=sub
                stu_info['subject']=sub
                stu_info['facult']=fac
                stu_dic[i]=stu_info

                print('>>>>>>>>>>>>>>>>>STU DATA<<<<<<<<<<<<<<<<<<<<<<<<')
                print(stu_dic)

            elif op == '2':
                sno = int(input("Enter sr no of the student you want to remove: "))
                if sno in stu_dic:
                    stu_dic.pop(sno)
                    print("Student removed successfully!")
                else:
                    print("Student not found")

            elif op == "3":
                print(stu_dic)

            elif op == "4":
                sno = int(input("Enter sr no of the student you want to view: "))
                if sno in stu_dic:
                    print('>>>>>>>>>>>>>>>>>STU DATA<<<<<<<<<<<<<<<<<<<<<<<<')
                    print(stu_dic[sno])
                else:
                    print("Student not found")

    elif choice == "2":
        op1 = input("faculty wants to perform any other operation? (Y/n) ")
        fac_dic = {}

        if op1 == "Y":
            sm1='''
                1. add marks to student
                2. view all student
            '''
            print(sm1)
            c1=input("Enter your choice: ")
            if c1 == "1":
                mm=int(input("Enter marks :"))
            elif c1 == "2":
                print(stu_dic)

    elif choice == "3":
        f = input("Enter first name: ")
        s = input("Enter your subject name here: ")
        m = int(input("Enter your marks here:"))
        c = int(input("Enter your contact details here:"))

        print(">>>>>>>>>>>>STU DATA<<<<<<<<<<<<<<<<<<<<<<")
        print(f)
        print(s)
        print(m)
        print(c)
        print("Thank you for providing your details here...")


main_menu()
