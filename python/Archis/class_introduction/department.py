class Department:
    def __init__(self,dept_name,HOD_name):
        self.HOD_name = HOD_name
        self.dept_name = dept_name

    
    def assign_course_to_professor(self,professor,course):

        prof_list = []
        course_list = []
        if professor.prof_name not in prof_list:
            prof_list.append(professor.prof_name) 
        for each in professor.subjects_taught:
            if each not in course_list:
                course_list.append(professor.prof_name)
        print (course_list)
        
    def __repr__(self):
        return 'Department = %s, HOD = %s'  % (self.dept_name , self.HOD_name)