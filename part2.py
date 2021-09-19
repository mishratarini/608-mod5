# Create a Dataframe grades for Student/grades

import pandas as pd

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
print(f'{grades_dict}')
grades = pd.DataFrame(grades_dict)
print(f'{grades}')

# Custom Indexes for Grades dictionary

grades.index = ['Test1', 'Test2', 'Test3']
print(f'{grades}')

# Grades for Eva
print(f'Grades for Mira : \n{grades["Eva"]}')

# Grades for Sam
print(f'Grades for Sam : \n{grades.Sam}')

# Grades for 1st Test using Loc[]
print(f'Grades for 1st Test using Loc[] : \n{grades.loc["Test1"]}')

# Grades for 1st Test using iLoc[]
print(f'Grades for 1st Test using iLoc[] : \n{grades.iloc[0]}')

# Slicing Grades to get Eva's second exam marks
print(f'Grades with AT : \n{grades.at["Test1", "Eva"]}')

# Slicing Grades to get Eva's second exam marks
print(f'Grades with iAT : \n{grades.iat[2, 0]}')

# Describe Grades
pd.set_option('precision',2)
print(f'Describe Grades : \n{grades.describe()}')

# Mean Grades
print(f'Mean of Grades : \n{grades.mean()}')

# Sorting Grades in reverse order
print(f'Sorting Grades in reverse : \n{grades.sort_index(ascending=False)}')

# Sorting Grades with Axis = 1
print(f'Sorting Grades in reverse : \n{grades.sort_index(axis=1)}')