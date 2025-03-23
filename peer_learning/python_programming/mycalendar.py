# 6. Python program to display calendar:
# It is simple in python programming to display calendar. To do so, you need to import the calendar module which comes with Python.

import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month:"))

print(calendar.month(yy, mm))

# end