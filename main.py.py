import numpy as np
import pandas as pd
# 1. LOAD DATASET
data = pd.read_csv('new_data.csv')
# 2. BASIC DATASET INFORMATION
print("Dataset Shape:")
print(data.shape)
print("\nColumn Names:")
print(data.columns)
print("\nFirst 5 Students:")
print(data.head())
# 3. CALCULATE TOTAL AND AVERAGE
subjects = ['Math', 'Python', 'DBMS', 'English']
data['Total2'] = data[subjects].sum(axis=1)
data['Average'] = data[subjects].mean(axis=1)
# 4. ASSIGN GRADES
grade_conditions = [
    data['Average'] >= 90,
    data['Average'] >= 80,
    data['Average'] >= 70,
    data['Average'] >= 60,
    data['Average'] >= 0
]

grades = ['A', 'B', 'C', 'D', 'F']

data['Grade'] = np.select(
    grade_conditions,
    grades,
    default='Not Graded'
)
# 5. PASS / FAIL RESULT
data['Result'] = np.where(
    data['Average'] >= 40,
    'pass',
    'fail'
)
# 6. PERFORMANCE CATEGORY
category_conditions = [
    data['Average'] >= 90,
    data['Average'] >= 80,
    data['Average'] >= 70,
    data['Average'] >= 60,
    data['Average'] >= 40
]

categories = [
    'Excellent',
    'Good',
    'Average',
    'Poor',
    'Needs Improvement'
]

data['Category'] = np.select(
    category_conditions,
    categories,
    default='Fail'
)
# 7. STUDENT RANK
data['Rank'] = data['Average'].rank(
    ascending=False,
    method='min'
).astype(int)

# 8. DISPLAY COMPLETE DATA
print("\nComplete Student Data:")
print(data)
# 9. TOP STUDENT
top_index = data['Average'].idxmax()

print("\nTop Student:")
print(data.loc[
    top_index,
    ['Name', 'Average', 'Grade']
])
# 10. LOWEST PERFORMING STUDENT

lowest_index = data['Average'].idxmin()

print("\nLowest Performing Student:")
print(data.loc[
    lowest_index,
    ['Name', 'Average', 'Grade']
])

# 11. TOP 5 STUDENTS

top_students = data.sort_values(
    by='Average',
    ascending=False
).head(5)

print("\nTop 5 Students:")
print(top_students[['Name', 'Average', 'Grade', 'Rank']])
# 12. SUBJECT AVERAGES

subject_avg = data[subjects].mean(axis=0)

print("\nSubject Averages:")
print(subject_avg)


best_subject = subject_avg.idxmax()
worst_subject = subject_avg.idxmin()

print("\nBest Subject:", best_subject)
print("Best Subject Average:", subject_avg[best_subject])

print("\nWorst Subject:", worst_subject)
print("Worst Subject Average:", subject_avg[worst_subject])
# 13. GRADE DISTRIBUTION
print("\nGrade Distribution:")
print(data['Grade'].value_counts())
# 14. RESULT DISTRIBUTION
print("\nResult Distribution:")
print(data['Result'].value_counts())
# 15. STUDENTS NEEDING IMPROVEMENT
students_need_improvement = data[
    data['Average'] < 70
]

print("\nStudents Needing Improvement:")
print(
    students_need_improvement[
        ['Name', 'Average', 'Grade', 'Result']
    ]
)
# 16. AVERAGE BY GRADE
grade_subject_avg = data.groupby('Grade')[subjects].mean()

print("\nSubject Average by Grade:")
print(grade_subject_avg)
# 17. SUBJECT FAILURE COUNT
failure_count = (
    data[subjects] < 40
).sum()

print("\nStudents Failing Each Subject:")
print(failure_count)
# 18. CLASS SUMMARY
total_students = len(data)

class_average = data['Average'].mean()

highest_average = data['Average'].max()

lowest_average = data['Average'].min()

pass_count = (data['Result'] == 'pass').sum()

fail_count = (data['Result'] == 'fail').sum()

pass_percentage = (pass_count / total_students) * 100


print("\n" + "=" * 45)
print("        STUDENT PERFORMANCE SUMMARY")
print("=" * 45)

print("Total Students      :", total_students)
print("Class Average       :", round(class_average, 2))
print("Highest Average     :", highest_average)
print("Lowest Average      :", lowest_average)
print("Best Subject        :", best_subject)
print("Worst Subject       :", worst_subject)
print("Students Passed     :", pass_count)
print("Students Failed     :", fail_count)
print("Pass Percentage     :", round(pass_percentage, 2), "%")

print("=" * 45)