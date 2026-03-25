import csv


# Function that allows user to input student names and grades and creates a file
def write_grades():
    # Ask the user for the number of students
    num_students = int(input('Enter the number of students: '))

    # Open the file with the "with" keyword
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # For loop to collect the name and grades for each student
        for i in range(num_students):
            print(f'\nEntering the data for student {i + 1}:')
            first = input('First Name: ')
            last = input('Last name: ')

            exam1 = int(input('Exam 1 grade: '))
            exam2 = int(input('Exam 2 grade: '))
            exam3 = int(input('Exam 3 grade: '))

            # Write a row for each student and their grades
            writer.writerow([first, last, exam1, exam2, exam3])

    print('The file has been created')

write_grades()