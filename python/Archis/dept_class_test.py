from dept_class import Professor
from dept_class import Student
from dept_class import Course
from dept_class import Department
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


    prof1 = Professor('Kishor',['EDC','VLSI'])
    prof2 = Professor('Vilas',['SS'])

    dept = Department()
    dept.assign_course_to_professor(prof1)
    dept.assign_course_to_professor(prof2)

    print (dept)


    print (prof1)
    print (prof2)