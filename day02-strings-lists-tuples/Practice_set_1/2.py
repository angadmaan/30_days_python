# Write a program to fill in a letter template which looks like below:
# letter = '''Dear <|NAME|>,
# You are selected!
# <|DATE|>'''   

name = input("Enter your name: ")
date = input("Enter the date: ")

letter = f'''Dear {name},
You are selected!
{date}'''

print(letter)