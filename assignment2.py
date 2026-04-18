class student ():
    def __init__ (self,student_name,roll_no,marks_sem1,marks_sem2):
         self.student_name=student_name
         self.roll_no= roll_no
         self.marks_sem1=marks_sem1
         self.marks_sem2=marks_sem2
    def calculate (self):
        self.c=(self.marks_sem1+self.marks_sem2)/2
        
    def student_info(self):
        input1=input("ENTER YOUR NAME:")
        input2=int(input("ENTER YOUR ROLL NO. :"))
        if input1==self.student_name and input2==self.roll_no:
            print(self.student_name)
            print("Sem1 SGPA:",self.marks_sem1)
            print("Sem2 SGPA:",self.marks_sem2)
            print("CGPA is :",self.c)
        else:
            print("INVALID USERNAME AND PASSWORD")
stu1=student("SUYASH KAMBLE",33,8.5,9.5)
stu1.calculate()
stu1.student_info()
