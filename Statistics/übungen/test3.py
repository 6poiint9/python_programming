


def square_numbers(numbers): 
    for num in numbers:
        print(num*num) 


num_list = [2, 4, 6, 8] 

square_numbers(num_list)

print(len(num_list))

print(num_list[2])

print(num_list[-1])

print("Student grades!\n")



student_grades = {
    "Mark" : (1, 3, 4, 3.5),
    "Eve"  : (1, 2, 1.5, 1), 
    "Lois" : (2, 1, 3, 2.25)
}

def average_grade(student_name):
    if student_name in student_grades:
         grades = student_grades[student_name] 
         return sum(grades) / len(grades)
    else: 
     print("student not found") 


print(average_grade("Mark"))
