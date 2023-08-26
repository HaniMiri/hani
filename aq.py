# class Employee:
#     name = input("Enter a name :")
#     employee_id=int(input("Enter a id :"))
#     department=input("Enter a department :")
#     salary=int(input("Enter a salary :"))
#     def __int__(self,name,employee_id,department,salary):
#         self.name=name
#         self.employee_id = employee_id
#         self.department = department
#         self.salary = salary
#     def Displayinfo(self):
#         print("the datd of employee is ",self.name," , ",self.employee_id," , ",self.department," , ",self.salary)
#     def   Rais_salary(self,amount):
#         self.salary += amount
#         return self.salary
# q= Employee()
# q.Displayinfo()
# print(q.Rais_salary(10))



# class Employee :
#     def __init__(self,name,id,dapartment,salary):
#         self.name=name
#         self.id=id
#         self.department=dapartment
#         self.salary=salary
#     def dispay(self):
#         print(f"name of employee: {self.name} \n id of the employee: {self.id}\ndepartment of the employee :{self.department}\n salary of the employee :{self.salary}")
#     def p(self,amount):
#         r=self.salary*amount/100
#         self.salary+=r
# emplyee=Employee('mohammed',20220882,'gaza',2500)
# emplyee.dispay()
# emplyee.p(10)




# class bank :
#
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.employee_id = id
#         self.salary = salary
#         self.list1=[]
#         self.list2=[]
#     def deposite (self,amount):
#         self.salary += amount
#         self.list1.append(f" diposite = {amount}  ")
#         return self.salary
#
#     def withdrawal (self,amount):
#         self.salary -= amount
#         self.list2.append(f" withdrawal = {amount}  ")
#         return self.salary
#
#     def print_deposite (self):
#         for i in self.list1:
#             print(i)
#     def print_withdrawal (self):
#         for i in self.list2:
#             print(i)
# name = input("Enter a name :")
# id = (input("Enter a id :"))
# salary = int(input("Enter a salary :"))
# q=bank(name,id,salary)
# q.deposite(200)
# q.deposite(2100)
# q.print_deposite()




# class Question :
#     def __init__(self,question,answers,correct_answer):
#         self.question = question
#         self.answers = answers #List
#         self.correct_answer = correct_answer
#
# class Quiz:
#     def __init__(self):
#         self.questions = []
#         self.score = 0
#
#     def add_question(self,question):
#         self.questions.append(question)
#
#     def display_quiz(self):
#         for q in self.questions:
#             print(q.question)
#             x = 1
#             for answer in q.answers:
#                 print(f"{x}-{answer}")
#                 x += 1
#             user_answer = int(input(">> Enter Your choice :"))
#             if user_answer == q.correct_answer :
#                 self.score += 1
#
#     def display_score(self):
#         print(f"** Your Score is :{self.score}/{len(self.questions)} ") # 5/10
#
#
# quiz = Quiz()
# q1 = Question ("What is your mentor name?",["Ghydaa","Reem","Mohannad","Zakaria"],1)
# q2 = Question ("What is your mentor name?",["Ghydaa","Reem","Mohannad","Zakaria"],2)
# q3 = Question ("What is your mentor name?",["Ghydaa","Reem","Mohannad","Zakaria"],3)
# q4 = Question ("What is your mentor name?",["Ghydaa","Reem","Mohannad","Zakaria"],4)
#
# quiz.add_question(q1)
# quiz.add_question(q2)
# quiz.add_question(q3)
# quiz.add_question(q4)
#
# quiz.display_quiz()
# quiz.display_score()




class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.employee_id,=id
        self.salary=salary
    def display_details(self):
        print(f"Employee name : {self.name}\nEmployee id : {self.employee_id}\nEmployee salar : {self.salary}")
class Manager(Employee):
    def __init__(self,name,id,salary,department):
        super().__init__(name,id,salary)
        self.department = department
    def display_details(self):
       print(f"Manager name: {self.name}\nManager id : {self.employee_id}\nManager salary {self.salary}\nManager department {self.department}")
class Engineer(Employee):
    def __init__(self,name,id,salary,programming_language):
        super().__init__(name,id,salary)
        self.programming_language = programming_language
    def display_details(self):
        print(f"Engineer name: {self.name}\nEngineer id : {self.employee_id}\nEngineer salary {self.salary}\nProgramming language :{self.programming_language}")
m=Manager('Hani',132,80000,'Gaza')
m.display_details()
eng1=Engineer('saly',18,448484,'java')
eng1.display_details()
emp1=Employee('Mohammed',99,74136)
emp1.display_details()






class Email:
    def __init__(self,sender, recipient, title, body,  is_new):
        self.sender=sender
        self.recipient=recipient
        self.title=title
        self.body=body
        self.is_new=is_new
    def display_details(self):
        print(f"Sender : {self.sender}\nRecipient : {self.recipient}\nTitle : {self.title}\nBody : {self.body}\nIs new : {self.is_new}")
class Inbox():
    listofemails=[]
    def add_emails(self,sender, recipient, title, body, is_new):
        email=Email(sender, recipient, title,body,is_new)
        self.listofemails.append(email)
    def display_emails(self):
        for e in self.listofemails:
            e.display_details()
    def open_email(self,index):

       self.listofemails[index-1].display_details()

user1=Inbox()
while True:
   Input =int( input('''1-Add Email
2-Show Emails
3-Open Email
4-Exit
Enter your choice : '''))
   if Input==1:
       sender=input("Enter sender : ")
       recipient=input('Enter recipient : ')
       title=input('Enter title : ')
       body=input('Enter body : ')
       is_new=bool(input('Enter whether its new : '))
       user1.add_emails(sender,recipient,title,body,is_new)
   elif Input==2:
       user1.display_emails()
   elif Input==3:
        e=int(input("Enter Number"))
        user1.open_email(e)
   elif Input == 4:
       break
   else:
       print("** Invalid Input **")