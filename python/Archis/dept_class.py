class Course:
    def __init__(self,course_name,semester,capacity = 10):
        self.course_name = course_name
        self.semester = semester
        self.enrollments = []
        self.capacity = capacity
    def __repr__(self):
        return 'Course name = %s , Semester = %s , Enrollments = %s, count = %s' % (self.course_name , self.semester , self.enrollments, len(self.enrollments))


class Student:
    def __init__(self,name,roll_no,year):
        self.name = name
        self.roll_no = roll_no
        self.year = year
        self.enrolled_courses = []

    def enroll_to_course(self,course):
        if len(course.enrollments) < course.capacity:
            if course not in self.enrolled_courses:
                self.enrolled_courses.append(course)
                course.enrollments.append(self)
        else:
            print ("Cannot enroll student: ",self.name)

    def __repr__(self):
            return 'Student Name = %s , Roll_no = %d , Year_studying_in = %s , enrolled_course = %s' % (self.name , self.roll_no , self.year , self.enrolled_courses)


if __name__ == "__main__":

    course1 = Course('VLSI','VII',2)
    course2 = Course('EDC','IV',3)
    course3 = Course('SS','III',2)
    
    stud = Student('Archis' , 6125 , 'BE')
    stud1 = Student('Vikram',6122 , 'BE')
    #stud2 = Student('Arnav', 5170 , 'TE')
    #stud3 = Student('soham', 6116,'BE')
    
    stud.enroll_to_course(course1)
    stud1.enroll_to_course(course1)
    #stud2.enroll_to_course(course2)
    
    print (course1)
    #print (course2)
    #print (course3)