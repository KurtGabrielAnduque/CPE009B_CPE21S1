
grade_input = int(input("Enter your grade to determine: "))

if grade_input >= 75:
    print('passed')    
elif grade_input == 74:
    print('Remedial')
elif grade_input < 0:
    print('dont input negative number')
elif grade_input < 74 and grade_input >= 0:
    print('Failed')
else: 
    print('Invalid input pls input number!!!!')