from models.student import add_students, students  
from models.course import register,  print_pairs, s_search

def main():

    s_num = add_students()
    
    for i in range(s_num):
        register(students)

    print_pairs()
    s_search()

if __name__ == "__main__":
    main()

