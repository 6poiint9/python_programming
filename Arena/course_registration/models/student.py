students = set()

s_num = 0 

def add_students() -> int:
    global s_num
    s_num = int(input("enter number of students to add: "))
    for i in range(s_num): 
        s_name = input(f'Enter name of student {i + 1}: ')
        students.add(s_name)
    return s_num 

