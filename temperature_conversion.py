#the following code will convert temperature in Fahrenheit to Celcius and Vise versa based on the input by the user
#the user will pick between option 1, F to C, or option 2, C to F
print('Type 1 for Fahrenheit to Celcius conversion')
print('Type 2 for Celcius to Fahrenheit conversion')
user_input = int(input())
#The following is where calculations are done (note that the end result will be rounded up to the nearest whole number)
if user_input == 1:
   F = float(input('What is your temperature (˚F)?: '))
   Convertion = (F-32)*(5/9)
   print(f'{F}˚F = {round(Convertion)} ˚C')
elif user_input == 2:
    C = float(input('What is your temperature (˚C)?: '))
    Convertion = (C*(9/5))+32
    print(f'{C}˚C = {round(Convertion)} ˚F')
else:
    print("input either 1 or 2")

input('Enter anything to close')