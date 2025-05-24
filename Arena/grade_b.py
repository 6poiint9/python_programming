# Student-Grade manager 
# Get input for: Name, 3-Grades 
# store grades as a list 
# => store in a dict 
# create a function to return Grade-average 
# 
def get_input() -> int: 
    add = int(input("please enter number of students to add: ")) 
    return add

def calculate_print_average(grades: dict[str, list[int]]) -> None: 
    for name, grade in grades.items():
            avg = float(sum(grade) / len(grade))
        #avg_book = {name: avg}
            print(f'{name}: average = {avg:.2f}')
            #return avg 

def search_print(grade_book: dict[str, list[int]]) -> None: 
        name = input("Enter name to search for: ").strip()
        if name in grade_book:
            print(f'Grades for {name}: {grade_book[name]}') 
        else:
            print("name not found")
        


def main(): 

    grade_book = {} 
    grades = []
    npc = 1

    add = get_input()

    while add > 0: 
        name = input(f'Enter name of Student {npc}: ').strip()
        a, b, c = map(int, input("Enter 3 Grades: ").split())
    
        # needs to be overwritten 
        grades = [a, b, c]
    
        grade_book[name] = grades

        add -= 1 
        npc += 1

    calculate_print_average(grade_book)

    search_print(grade_book)




if __name__ == "__main__":
   main()


