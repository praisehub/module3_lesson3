#Parent class Students
class Students:
 def __init__(self, first, last,):
   self.first = first
   self.last = last
   self.email = first + '.' + last + "@stutern.com"
   
 def fullname(self):
    return "{} {}". format(self.first, self.last)
  
   #1 CREATING SUBCLASS GROUPLEADER
class Group_Leader(Students):
  def __init__(self, first, last, students=[]):
   super().__init__(first, last)
   self.students = students
       
#2 METHOD THAT ADDS STUDENTS TO GROUP_LEADER LIST
  def add_students(self, students):
   self.students.append(students)
   print(f"student {students} add to Group_leader list")
  

 #3 METHOD THAT REMOVES STUDENTS FROM GROUP_LEADER LIST   
  def remove_students(self, students):
   self.students.remove(students)
   print(f"student {students} removed from Group_Leader list")
   
#4 CREATING 5INSTANCES OF THE PARENT CLASS
print(f" FIVE INSTANCES OF PARENT CLASSS\n{'-' * 100}")
student1 = Students('Ahmed', 'Salihu')
print(1, student1.first,'\t\t', student1.last, '\t\t', student1.email)
print()
  
student2 = Students('Bamidele', 'Kolawole')
print(2, student2.first, '\t\t', student2.last, '\t\t', student2.email)
print()
  
student3 = Students('Anita', 'Ojo')
print(3, student3.first, '\t\t', student3.last, '\t\t', student3.email)
print()
  
student4 = Students('Samir', 'Ameen')
print(4, student4.first, '\t\t', student4.last, '\t\t', student4.email)
print()
  
student5 = Students('Linda', 'Parson')
print(5, student5.first, '\t\t', student5.last, '\t\t', student5.email)
print()
  
  #5 GET FIRSTNAME, LASTNAME AND EMAIL OF STUDENT1 IN PARENT CLASS
print(f" DETAILS OF STUDENT 1 IN PARENT CLASS \n{'-' * 100}")

print(1, student1.first, '\t\t', student1.last, '\t\t', student1.email)
  
  #6 CREATING 2 INSTANCES OF THE SUBCLASS
print(f" 2 INSTANCES OF SUB CLASS GROUP_LEADER\n{'-' * 100}")
leader1 = Group_Leader('Mariam', 'Adeoti')
print(1, leader1.first, '\t\t', leader1.last, '\t\t', leader1.email)

leader2 = Group_Leader('Adaji', 'Rukayat')
print(2, leader2.first, '\t\t', leader2.last, '\t\t', leader2.email)
  
  #ADDING 2students to leader1
 
new_student1 = ('Ogunmola','Laide')
new_student2 = ('Adah', 'Uche')
  
  #ADDING 2STUDENTS TO LEADER2
new_student3 = ('Deborah', 'Andrew')
new_student4 = ('Joanna', 'Danladi')
  
  #7 CALLING THE ADD STUDENTS METHOD FOR THE 2 INSTANCES
print(f" ADDING STUDENTS TO 2 SUBCLASS LIST\n{'-' * 100}")
leader1.add_students(new_student1)
leader1.add_students(new_student2)
leader2.add_students(new_student3)
leader2.add_students(new_student4)

#8 REMOVING 1 STUDENT EACH FROM THE TWO INSTANCES
print(f" REMOVING 1 STUDENTS EACH FROM THE 2 SUBCLASS LIST\n{'-' * 100}")
leader1.remove_students(new_student1)
leader2.remove_students(new_student3)

#9FULL NAME OF STUDENTS UNDER INSTANCES OF SUBCLASS
#METHOD THAT PRINTS OUT FULLNAME 
def fullname(self):
    print(f"{self.first} {self.last}")

print(f"FULLNAME OF STUDENTS UNDER SUBCLASS LIST\n{'-' * 100}")    
print(leader1.fullname())
print(leader2.fullname())


print(f"EMAIL OF STUDENTS UNDER SUBCLASS LIST\n{'-' * 100}") 
print(leader1.email)
print(leader2.email)