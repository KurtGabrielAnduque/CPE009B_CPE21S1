grade_input = int(input("Enter your grade to determine: "))

if grade_input >= 75 and grade_input <= 100:
    print('passed')    
elif grade_input == 74:
    print('Remedial')
elif grade_input < 74 and grade_input >= 0:
    print('Failed')
else:
    print('===============================')
    print('Grades only range 0-100')
    print('Dont input negative number')
    print('===============================')
