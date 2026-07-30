#Initialize an empty dictionary
students = {}

#Function for valid float inputs
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")

#Function for valid int input
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Plese enter a whole number")

#Calculate average function
def calculate_average(grades_list):
    try:
        return sum(grades_list) / len(grades_list)
    except ZeroDivisionError:
        print("Error: No grades to average.")
        return 0.0

#Assign letter to average function
def assign_letter_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
    
def class_report(students):
    # loop through students.items()
    for student_id, info in students.items():
        print(f"student_ID: {student_id} | Name: {info["name"]} | Average: {round(info["average"], 2)} | Letter Grade: {info["letter_grade"]} | Passed: {info["passed"]} ")

#Main menu
#while True:


#Prompt user for number of students and number of grades
num_students = get_valid_int("Enter Number of Students: ")
num_grades = get_valid_int("Enter Number of Grades: ")
passing_score = get_valid_float("Enter the Passing Score (e.g., 50, 60, 70): ")

#Loop to collect data
#Loop that handles student one by one
for _ in range(num_students):
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    #Empty list to score the grades of each student
    grades_list = []

    #Inner loop to collect grades for each student
    for i in range(num_grades):
        score = get_valid_float(f"Enter grade {i+1} for {student_name}: ")
        grades_list.append(score)

    #Call calculate average function
    student_average = calculate_average(grades_list)

    #Call assign letter to average function
    student_letter = assign_letter_grade(student_average)

    
    #Use a boolean to determine if they passed
    #Stores True or False
    student_passed = student_average >= passing_score
    
    #Store all the collected data inside the main students dictionary
    students[student_id] = {
        "name": student_name,
        "scores": grades_list,
        "average": student_average,
        "passed": student_passed,
        "letter_grade": student_letter
        }
    
    print(students)
# print each student's name, average, letter grade, pass/fail
print("---FINAL REPORT----")
class_report(students)
