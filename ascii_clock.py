# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anthony Guzman, Dylan Duarte
# Assignment: ascii_clock.py
# Date:  31 October 2022

#the following is 5 dictionaries that define each number 0 to 9 (and colon) on each line of the clock
Clock1 ={'0':'000  ','1': ' 1   ', '2': '222  ', '3': '333  ', '4':'4 4  ','5': '555  ','6':'666  ','7':'777  ','8':'888  ','9': '999  ',':':'   '}
Clock2 = {'0':'0 0  ','1':'11   ','2':'  2  ','3':'  3  ','4':'4 4  ','5':'5    ','6':'6    ','7':'  7  ','8':'8 8  ','9':'9 9  ',':':' : '}
Clock3 = {'0':'0 0  ','1': ' 1   ', '2':'222  ', '3':'333  ', '4':'444  ','5':'555  ','6':'666  ','7':'  7  ','8':'888  ','9':'999  ',':':'   '}
Clock4 = {'0':'0 0  ','1':' 1   ','2':'2    ','3':'  3  ','4':'  4  ','5':'  5  ','6':'6 6  ','7':'  7  ','8':'8 8  ','9':'  9  ',':': ' : '}
Clock5 = {'0': '000  ','1':'111  ','2':'222  ','3':'333  ','4':'  4  ' 
,'5':'555  ','6':'666  ','7':'  7  ','8':'888  ','9':'999  ',':':'   '}

#the following takes user input
usertime = input('Enter a Time: ')

#the following will print the the time in ascii art
if len(usertime) == 4:
  print(f'{Clock1[usertime[0]]}{Clock1[usertime[1]]}{Clock1[usertime[2]]}{Clock1[usertime[3]]}')
  print(f'{Clock2[usertime[0]]}{Clock2[usertime[1]]}{Clock2[usertime[2]]}{Clock2[usertime[3]]}')
  print(f'{Clock3[usertime[0]]}{Clock3[usertime[1]]}{Clock3[usertime[2]]}{Clock3[usertime[3]]}')
  print(f'{Clock4[usertime[0]]}{Clock4[usertime[1]]}{Clock4[usertime[2]]}{Clock4[usertime[3]]}')
  print(f'{Clock5[usertime[0]]}{Clock5[usertime[1]]}{Clock5[usertime[2]]}{Clock5[usertime[3]]}')



else:
  print(f'{Clock1[usertime[0]]}{Clock1[usertime[1]]}{Clock1[usertime[2]]}{Clock1[usertime[3]]}{Clock1[usertime[4]]}')

  print(f'{Clock2[usertime[0]]}{Clock2[usertime[1]]}{Clock2[usertime[2]]}{Clock2[usertime[3]]}{Clock2[usertime[4]]}')

  print(f'{Clock3[usertime[0]]}{Clock3[usertime[1]]}{Clock3[usertime[2]]}{Clock3[usertime[3]]}{Clock3[usertime[4]]}')

  print(f'{Clock4[usertime[0]]}{Clock4[usertime[1]]}{Clock4[usertime[2]]}{Clock4[usertime[3]]}{Clock4[usertime[4]]}')

  print(f'{Clock5[usertime[0]]}{Clock5[usertime[1]]}{Clock5[usertime[2]]}{Clock5[usertime[3]]}{Clock5[usertime[4]]}')
