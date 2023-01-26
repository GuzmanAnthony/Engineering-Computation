# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   George Haddad,Omar Khalil,Anthony Guzman, Blake Gray, Dylan Duarte
# Assignment: Lab 5a Activity 2
# Date:  3 October 2022

# the code starts with our assigning values to the variables we've created
pts = 0 # pts will keep track of points, it starts at zero
sex = input('Enter your sex (m/f): ') # ask user for gender
age = int(input('Enter your age (years): ')) # ask user for age
if age < 20 or age > 79: # if age is outside the calculable range an error message is printed, code ends
    print('Risk % is not calculable given the inputted age, (age must be from 20 to 79)')
    quit()
smoke = input('Do you smoke? (y/n): ') # asks user if they smoke
chol = int(input('Enter total cholesterol (mg/dL): ')) # asks user for cholesterol
HDL = int(input('Enter your HDL cholesterol (mg/dL): ')) # asks user for HDL cholesterol
BP = int(input('Enter your systolic Blood Pressure (mmHg): ')) # asks user for systolic blood pressure
medicated = input('Are you taking blood pressure medication (y/n): ') # asks user if their medicated for BP
risk = 0 # risks starts at zero and is updated later once points are added up
age_range = 0 # age_range is used to group user into 1 of 5 groups, important for calculating smoke and cholesterol points
# the following is how we determine which age group the user should fall under
if age > 69:
    age_range = 1
elif age > 59:
    age_range = 2
elif age > 49:
    age_range = 3
elif age > 39:
    age_range = 4
elif age > 19:
    age_range = 5

# HDL point calculations as follows:
# HDL points are the same regardless of gender, therefore points calculated separate from gender
if HDL >= 60:
    pts -= 1
elif 50 <= HDL <= 59:
    pts += 0
elif 40 <= HDL <= 49:
    pts += 1
elif HDL < 40:
    pts += 2

if sex == 'm': #if statement for when user input 'm' for sex
    if age > 74: # points calculated accordingly based on age
        pts += 13
    elif age > 69:
        pts += 12
    elif age > 64:
        pts += 11
    elif age > 59:
        pts += 10
    elif age > 54:
        pts += 8
    elif age > 49:
        pts += 6
    elif age > 44:
        pts += 3
    elif age > 39:
        pts += 0
    elif age > 34:
        pts -= 4
    elif age > 19:
        pts -= 9

    if smoke == "y": # if user said they smoke points will be added accordingly
        if age_range == 1:
            pts += 1
        if age_range == 2:
            pts += 1
        if age_range == 3:
            pts += 3
        if age_range == 4:
            pts += 5
        if age_range == 5:
            pts += 8

    if age_range == 5: # based on users age_range, the calculations for cholesterol will differ
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 4
        elif 200 <= chol <= 239:
            pts += 7
        elif 240 <= chol <= 279:
            pts += 9
        elif chol >= 280:
            pts += 11
    if age_range == 4:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 3
        elif 200 <= chol <= 239:
            pts += 5
        elif 240 <= chol <= 279:
            pts += 6
        elif chol >= 280:
            pts += 8
    if age_range == 3:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 2
        elif 200 <= chol <= 239:
            pts += 3
        elif 240 <= chol <= 279:
            pts += 4
        elif chol >= 280:
            pts += 5
    if age_range == 2:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 1
        elif 200 <= chol <= 239:
            pts += 1
        elif 240 <= chol <= 279:
            pts += 2
        elif chol >= 280:
            pts += 3
    if age_range == 1:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 0
        elif 200 <= chol <= 239:
            pts += 0
        elif 240 <= chol <= 279:
            pts += 1
        elif chol >= 280:
            pts += 1
    # if taking BP medication the points for their BP will differ, it calculated accordingly.
    if medicated == "n":
        if BP <= 129:
            pts += 0
        if 130 <= BP <= 159:
            pts += 1
        if BP >= 160:
            pts += 2
    if medicated == "y":
        if BP <= 119:
            pts += 0
        if 120 <= BP <= 129:
            pts += 1
        if 130 <= BP <= 159:
            pts += 2
        if BP >= 160:
            pts += 3
    if pts < 0: # points are added and risk is given a value based on points
        risk = '<1%'
    elif pts == 0:
        risk = '1%'
    elif pts == 1:
        risk = '1%'
    elif pts == 2:
        risk = '1%'
    elif pts == 3:
        risk = '1%'
    elif pts == 4:
        risk = '1%'
    elif pts == 5:
        risk = '2%'
    elif pts == 6:
        risk = '2%'
    elif pts == 7:
        risk = '3%'
    elif pts == 8:
        risk = '4%'
    elif pts == 9:
        risk = '5%'
    elif pts == 10:
        risk = '6%'
    elif pts == 11:
        risk = '8%'
    elif pts == 12:
        risk = '10%'
    elif pts == 13:
        risk = '12%'
    elif pts == 14:
        risk = '16%'
    elif pts == 15:
        risk = '20%'
    elif pts == 16:
        risk = '25%'
    elif pts >= 17:
        risk = 'greater ≥ 30%'
    print('Your 10-year risk of a heart attack is', risk) # risk is printed

# female code is same as male except points and risk adjusted as necessary
if sex == 'f':
    if age > 74:
        pts += 16
    elif age > 69:
        pts += 14
    elif age > 64:
        pts += 12
    elif age > 59:
        pts += 10
    elif age > 54:
        pts += 8
    elif age > 49:
        pts += 6
    elif age > 44:
        pts += 3
    elif age > 39:
        pts += 0
    elif age > 34:
        pts -= 3
    elif age > 19:
        pts -= 7

    if smoke == "y":
        if age_range == 1:
            pts += 1
        if age_range == 2:
            pts += 2
        if age_range == 3:
            pts += 4
        if age_range == 4:
            pts += 7
        if age_range == 5:
            pts += 9

    if age_range == 5:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 4
        elif 200 <= chol <= 239:
            pts += 8
        elif 240 <= chol <= 279:
            pts += 11
        elif chol >= 280:
            pts += 13
    if age_range == 4:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 3
        elif 200 <= chol <= 239:
            pts += 6
        elif 240 <= chol <= 279:
            pts += 8
        elif chol >= 280:
            pts += 10
    if age_range == 3:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 2
        elif 200 <= chol <= 239:
            pts += 4
        elif 240 <= chol <= 279:
            pts += 5
        elif chol >= 280:
            pts += 7
    if age_range == 2:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 1
        elif 200 <= chol <= 239:
            pts += 2
        elif 240 <= chol <= 279:
            pts += 3
        elif chol >= 280:
            pts += 4
    if age_range == 1:
        if chol < 160:
            pts += 0
        elif 160 <= chol <= 199:
            pts += 1
        elif 200 <= chol <= 239:
            pts += 1
        elif 240 <= chol <= 279:
            pts += 2
        elif chol >= 280:
            pts += 2
    # BP
    if medicated == "n":
        if BP < 120:
            pts += 0
        if 120 <= BP <= 129:
            pts += 1
        if 130 <= BP <= 139:
            pts += 2
        if 140 <= BP <= 159:
            pts += 3
        if BP >= 160:
            pts += 4
    if medicated == "y":
        if BP < 120:
            pts += 0
        if 120 <= BP <= 129:
            pts += 3
        if 130 <= BP <= 139:
            pts += 4
        if 140 <= BP <= 159:
            pts += 5
        if BP >= 160:
            pts += 6
    if pts < 9:
        risk = '<1%'
    elif pts == 9:
        risk = '1%'
    elif pts == 10:
        risk = '1%'
    elif pts == 11:
        risk = '1%'
    elif pts == 12:
        risk = '1%'
    elif pts == 13:
        risk = '2%'
    elif pts == 14:
        risk = '2%'
    elif pts == 15:
        risk = '3%'
    elif pts == 16:
        risk = '4%'
    elif pts == 17:
        risk = '5%'
    elif pts == 18:
        risk = '6%'
    elif pts == 19:
        risk = '8%'
    elif pts == 20:
        risk = '11%'
    elif pts == 21:
        risk = '14%'
    elif pts == 22:
        risk = '17%'
    elif pts == 23:
        risk = '22%'
    elif pts == 24:
        risk = '27%'
    elif pts >= 25:
        risk = 'greater ≥ 30%'
    print('Your 10-year risk of a heart attack is', risk)

input('Press Enter to close')
