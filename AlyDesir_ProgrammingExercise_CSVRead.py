import csv


# Function that reads the grade data and prints it in a table
def read_grades():
    # Open and read the CSV file
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)

        # Covert the data to a list to make it into readable rows
        data = list(reader)

        print('\n Student Grades\n')
        print(f" {'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")

    print('---------------------------------------------------')

    # Loop through each row in the data apart from the header
    for row in data[1:]:
        print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

read_grades()