# Create a series grades from list of integers
import pandas as pd

grades = pd.Series([87, 100, 94])

# Get the 1st values of Grades series
print(f'First Value of Grade is {grades[0]}')

# Calling the built in series functions:
print(f'Count of Grades is {grades.count()}')
print(f'Mean of Grades is {grades.mean()}')
print(f'min of Grades is {grades.min()}')
print(f'max of Grades is {grades.max()}')
print(f'STD of Grades is {grades.std()}')

print(f'Description of Grades : \n{grades.describe()}')

# Initialize Grades with a dictionary using {Student name : Exam score}
grades_dict = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
print(f'{grades_dict}')

#  Eva's score by calling grades['Eva']
print(f'Score of Eva: {grades_dict["Eva"]}')

# Wally's score using dot notation: grades.Wally.
print(f'Score of Wally with DOT notation: {grades_dict.Wally}')

# Series values attribute to view the array of values
print(f'Array of Values: {grades_dict.values}')
