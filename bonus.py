import re
import pandas as pd

# Create a dictionary of City-Zip
zips = pd.Series({'Boston': '02215', 'Miami': '3310'})
print(f'Zips:\n{zips}')

# Check for 5 digit zip code
print(zips.str.match(r'\d{5}'))

# Create a Series Cities
cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])
print(f'cities:\n{cities}')

# Evaluate Series with contains
print(cities.str.contains(r' [A-Z]{2} '))

# Evaluate Series with match
print(cities.str.match(r' [A-Z]{2} '))

# Create contactsdf DataFrame from a two-dimensional array
contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'], ['Sue Brown', 'demo2@deitel.com', '5555551234']]
contactsdf = pd.DataFrame(contacts, columns=['Name', 'Email', 'Phone'])
print(f'contactsdf : \n{contactsdf}')


# Format phone numbers from contactsdf DataFrame 
def get_formatted_ph(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value


formatted_phone = contactsdf['Phone'].map(get_formatted_ph)
print(f'Formatted Phone numbers for Contacts : \n{formatted_phone}')
