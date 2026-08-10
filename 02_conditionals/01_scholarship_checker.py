# If, Elif, Else / And, Or
# Scholarship Eligibility Checker

student_name = input("What is your name? ")
student_gpa = float(input("What is your GPA? "))
sat_score = int(input("What is your SAT score? "))

if student_gpa >= 3.8 and sat_score >= 1400:
    print("Full Scholarship")
elif student_gpa >= 3.5 and sat_score >= 1200:
    print("Partial Scholarship")
else:
    print("No Scholarship")