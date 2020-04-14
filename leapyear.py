a = int(input('Enter the Year:'))
if (year % 4 == 0):
  if (year % 400 == 0):
    print('Non Leap Year')
  else:
    print('Leap Year')
else:
  print('Non Leap Year')
