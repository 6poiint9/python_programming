
sc_pairs = {}

courses = {"oos2", "databases", "Typescript", "OS2"}

students = set()

s_num = 0 


def add_students():
    global s_num
    s_num = int(input("enter number of students to add: "))
    for i in range(s_num): 
        s_name = input(f'Enter name of student {i + 1}: ')
        students.add(s_name)



def register() -> None: 
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

def main():
    # your main program logic here
    
    add_students()
    
    for i in range(s_num):
        register() 

    print_pairs()
    
    s_search()

    
if __name__ == "__main__":
    main()
