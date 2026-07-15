# Write a program to find out whether student passed or failed if it requires a total of 40% and 33% atleast in each subject to pass. Assume 3 subjects and take marks  as an input from user.

marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 = int(input("Enter marks3: "))

total_percentage = (marks1+marks2+marks3)/3

if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Pass", total_percentage)
else:
    print("Fail", total_percentage)

    

