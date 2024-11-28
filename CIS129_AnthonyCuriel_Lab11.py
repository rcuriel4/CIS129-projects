#9.1 write grades to a plain text file
def store_grades():
    with open('grades.txt', 'w') as file:
        while True:
            grade = int(input('Enter a grade (enter -1 to stop): '))
            
            if grade == -1:
                break
            file.write(f'{grade}\n')
    print('The grades have been saved to grades.txt')
    
store_grades()
    
    
#9.2 read grades from the plain text file
#Display individual grades, total, count, and average
#look back at module 5 for individual grades
def read_grades():
    total = 0
    grade_count = 0
    grades = []
    
    try:
        with open('grades.txt', 'r') as file:
            for line in file:
                grade = int(line.strip())
                grades.append(grade)
                total += grade
                grade_count += 1       
                 
        if grade_count != 0:
            average = total / grade_count
            print(f'Individual grades: {grades}', f'\nTotal grades: {total}', f'\nNumber of grades: {grade_count}', f'\nAverage grade: {average:.2f}')
            
        else:
            print('No grades were found in the file.')
    
    except FileNotFoundError:
        print('File grades.txt does not exist.')
        
read_grades()
        

#9.3 write student records to a csv file
import csv
#start here again, to make it look better
def student_records():
    with open('grades.csv', mode = 'w', newline = '') as file:
        writer =  csv.writer(file)
        #header for neatness
        writer.writerow(['First Name','Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
        
        while True:
            firstName = input("Enter student's first name (enter 'exit' to stop): ")
            if firstName.lower() == 'exit':
                break
            
            lastName = input("Enter student's last name: ")
            exam1 = int(input('Enter Exam 1 grade: '))
            exam2 = int(input('Enter Exam 2 grade: '))
            exam3 = int(input('Enter Exam 3 grade: '))
            
            writer.writerow([firstName, lastName, exam1, exam2, exam3])
            
        print('Student records have been saved to grades.csv.')
        
student_records()