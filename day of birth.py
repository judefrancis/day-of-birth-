from datetime import date
import calendar
current_year=int(input("Enter current year; "))
day=int(input("Enter date of birth(1-31); "))
month=int(input("Enter the month you were born in(1-12); "))
age=int(input("Enter your age; "))
x=int(input("Enter 1 if your birthday has passed this year else 2"))
if x==1:
  year=current_year-age
else:
  year=current_year-age-1
birthday=date(year, month, day)
print(birthday.strftime("You were born on %d %A %b %Y"))
input("Press enter")
