courses = {"oos2", "databases", "Typescript", "OS2"}

sc_pairs = {}

def register(students: set) -> None: 
    # 
    s_name = input("Enter name of student to register: ")
    if s_name in students: 
        s_course = input(f'Enter course to join {print(courses)} : ')
        if s_course in courses: 
            #add student and course to dict 
            sc_pairs[s_name] = s_course         
        else:
            print("course name not found!")
    else:
        print("student name not found") 


def print_pairs():
    for name, course in sc_pairs.items():
        print(f'Student: {name}')
        print(f'Course: {course}')
        print(" ")

def s_search():
    s_name = input("Enter student name to search for: ")
    if s_name in sc_pairs:
        print(f' Course: {sc_pairs[s_name]}')
    else:
        print("student not found!")

 
