class Subject:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'Subject name = %s' % (self.name)

class Course:
    def __init__(self,course_name,semester,enrollments = 0):
        self.course_name = course_name
        self.semester = semester
        self.enrollments = enrollments

    def print_all(self):
        print (self.__class__.in)
    def __repr__(self):
        return 'Course name = %s , Semester = %s , Enrollments = %d' % (self.course_name , self.semester , self.enrollments)


class Student:
    def __init__(self,name,roll_no,year,course_chosen):
        self.name = name
        self.roll_no = roll_no
        self.year = year
        self.course_chosen = course_chosen

    def enrolled_to_course(self):
        if self.course_chosen == self.course_name:
            self.enrollments += 1

    def __repr__(self):
        return 'Student Name = %s , Roll_no = %d , Year_studying_in = %s , course_Chosen = %s' % (self.name , self.roll_no , self.year , self.course_chosen)

class Professor:
    def __init__(self,name,subjects):
        self.name = name 
        self.subjects = subjects

    def __repr__(self):
        return 'Professor Name = %s , Subjects_taught = %s' % (self.name,self.subjects)


if __name__ == "__main__":

    course1 = Course('VLSI', 'VII')
    course2 = Course('EDC', 'VI')
    course3 = Course('DE' , 'III')
    stud = Student('Archis' , 6125 , 'BE' , 'VLSI')
    stud1 = Student ('Vikram',6122 , 'BE', 'EDC')
    stud2 = Student('Arnav', 5170 , 'TE' , 'DE' )
    stud3 = Student('Soham', 6177,'TE' , 'SS')
    #stud4 = Student('Vijay' , 6546 , 'BE')
    stud.enrolled_to_course()
    print (course1.__repr__())