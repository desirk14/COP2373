import csv
import numpy as np

# Function that loads the exam grades from the file
def load_grades(filename):
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            # Convert columns to integers
            exam1 = int(row[2])
            exam2 = int(row[3])
            exam3 = int(row[4])

            # Add row of grades
            data.append([exam1, exam2, exam3])

    # Convert the list of Python lists into a NumPy array
    return np.array(data)


# Function that prints the statistics for each exam and across all exams
def print_statistics(data):
    exam_names = ['Exam 1', 'Exam 2', 'Exam 3']

    print('Statistics by Exam:\n')

    for i in range(3):
        exam_scores = data[:, i]

        print(exam_names[i])

        # Print the mean, median, min, max, and standard deviation
        print('Mean:', np.mean(exam_scores))
        print('Median:', np.median(exam_scores))
        print('Min:', np.min(exam_scores))
        print('Max:', np.max(exam_scores))
        print('Std Dev:', np.std(exam_scores))

    print('Overall Statistics (All Exams Combined):\n')

    # Flatten 2D array into 1D list of all scores
    all_scores = data.flatten()

    print('Overall Mean:', np.mean(all_scores))
    print('Overall Median:', np.median(all_scores))
    print('Overall Min:', np.min(all_scores))
    print('Overall Max:', np.max(all_scores))
    print('Overall Std Dev:', np.std(all_scores))

    print('Pass/Fail Counts:\n')

    for i in range(3):
        exam_scores = data[:, i]

        passed = np.sum(exam_scores >= 60)
        failed = np.sum(exam_scores < 60)

        print(f'{exam_names[i]}: Passed = {passed}, Failed = {failed}')

    # Find overall pass percentage across all exams
    total_scores = data.size

    total_passes = np.sum(data >= 60)

    pass_percent = (total_passes / total_scores) * 100

    print('\nOverall Pass Percentage:', round(pass_percent, 2), '%')

#Main function
def main():
    filename = 'grades.csv'

    data = load_grades(filename)

    print('First five rows of data:')
    print(data[:5], '\n')

    # Compute and print all stats calculated previously
    print_statistics(data)

main()
