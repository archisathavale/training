class Course:
    #Initiating constructor of class Course 
    def __init__(self,course_name,semester,capacity = 10):
        self.course_name = course_name
        self.semester = semester
        self.capacity = capacity
        #Creating empty list to store enrollments of students in a course
        self.enrollments = []
    #repr function for representing course details     
    def __repr__(self):
        enrolls = []
        for each in self.enrollments:
            #Appending only roll_nos of students in course details
            enrolls.append(str(each.roll_no))
        a = ",".join(enrolls)
        return 'Course name = %s , Semester = %s , Enrollments = %s, count = %s' % (self.course_name , self.semester , a , len(self.enrollments))


class Student:
    #Initiating constructor of class Student
    def __init__(self,name,roll_no,year):
        self.name = name
        self.roll_no = roll_no
        self.year = year
        #Empty list for storing courses 
        self.enrolled_courses = []
        self.courses_names_list = []
        self.student_names_list = []
    #creating a method for a student to enroll for a course
    def enroll_to_course(self,course):
        #List of current semesters
        current_semester = ['I','III','V','VII']
        #Condition for checking the course capacity
        if len(course.enrollments) < course.capacity:
            #Checking the course availability on the basis of year
            if self.year == 'BE':
                #Checking the availability on the basis of semester
                if course.semester == 'VII' or course.semester == 'VIII': 
                    if course.semester in current_semester:
                    #Appending the selected course in the enrolled_courses list
                        self.enrolled_courses.append(course)
                    #Appending all student objects in the course enrollments list  
                        course.enrollments.append(self)
                    else:
                        print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                else:
                    print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year)

            elif self.year == 'TE':
                if course.semester == 'V' or course.semester == 'VI':
                    if course.semester in current_semester:
                        self.enrolled_courses.append(course)
                        course.enrollments.append(self)
                    else:
                        print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                else:
                    print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year)

            elif self.year == 'SE':
                if course.semester == 'III' or course.semester == 'IV':
                    if course.semester in current_semester:
                        self.enrolled_courses.append(course)
                        course.enrollments.append(self)
                    else:
                        print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                else:
                    print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year)

            elif self.year == 'FE':
                if course.semester == 'I' or course.semester == 'II':
                    if course.semester in current_semester:
                        self.enrolled_courses.append(course)
                        course.enrollments.append(self)
                    else:
                        print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                else:
                    print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year)
            
        else:
            print ("Cannot enroll student: ",self.name , 'capacity is full')
    #repr function for representing student data
    def __repr__(self):
        enrolls = []
        for each in self.enrolled_courses:
            #Appending only course_name in student details
            enrolls.append(str(each.course_name))
        a = ",".join(enrolls)
        return 'Student Name = %s , Roll_no = %d , Year_studying_in = %s , enrolled_course = %s' % (self.name , self.roll_no , self.year , a)
            
class Professor:
    def __init__(self,prof_name,subjects_teach):
        self.prof_name = prof_name
        self.subjects_teach = subjects_teach

    def assign_course_to_professor(self,subjects_teach):
        pass
if __name__ == "__main__":

    course1 = Course('VLSI','VIII',2)
    course2 = Course('EDC','IV',3)
    course3 = Course('SS','III',2)
    course4 = Course('Physics','I',5)
    course5 = Course('Microprocessor','V',2)
    course6 = Course('BCS','VII',3)
    course7 = Course('Maths','I',9)
    
    stud = Student('Archis' , 4125 , 'BE')
    stud1 = Student('Vikram',2122 , 'SE')
    stud2 = Student('Arnav', 3170 , 'TE')
    stud3 = Student('Vijay', 1962,'FE')
    stud4 = Student('Soham', 2990,'SE')
    stud5 = Student('Pranav', 3971,'TE')
    stud6 = Student('Viraj', 4987,'BE')
    stud7 = Student('Anil', 1910,'FE')
    stud8 = Student('Girish',3861,'TE')


    stud.enroll_to_course(course6)
    stud1.enroll_to_course(course3)
    stud2.enroll_to_course(course4)
    stud3.enroll_to_course(course4)
    stud4.enroll_to_course(course2)
    stud5.enroll_to_course(course5)
    stud6.enroll_to_course(course1)
    stud7.enroll_to_course(course5)
    stud3.enroll_to_course(course7)
    stud8.enroll_to_course(course5)


    print (course1)
    print (course2)
    print (course3)
    print (course4)
    print (course5)
    print (course6)
    print (course7)


    print (stud)
    print (stud1)
    print (stud2)
    print (stud3)
    print (stud4)
    print (stud5)
    print (stud6)
    print (stud7)
    print (stud8)