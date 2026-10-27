class Student:
    def __init__(self,name,admission_number,marks):
        self.name=name
        self.admission_number=admission_number
        self.marks=marks
        
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    def display_details(self):
        average=self.calculate_average()
        if average >=70:
            grade="A"
        if average >=60:
             grade="B"
        if average >=50:
            grade="C"
        if average>=40:
            grade="D"
        else:
            grade="E"
        print("\n---Student details---")
        print("Name:",self.name)
        print("Admission _number:",self.admission_number)
        print("Marks:",self.marks)
        print("Average:",round(average,3))
        print("Grade:",grade)


    def pass_status(self):
             average=self.calculate_average()
             if average>=40:
                  return"pass"
             else:
                  return"fail"
name=input("Enter name: ")
admission_number=int(input("Enter admission_number: "))

marks=[]
for i in range(3):
        mark=float(input("Enter mark for subject{i+1}:"))
        marks.append(mark)

student1=Student(name,admission_number,marks)
student1.display_details()
student1.pass_status()
            
print("status",student1.pass_status())                           
        
            
        