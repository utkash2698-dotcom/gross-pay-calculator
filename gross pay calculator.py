statement='what is hours worked?\n'
hours=input(statement)
statement2='what is your hourly rate?\n'
rate=input(statement2)
try:
    gross_pay = float(hours) * float(rate)
    print('your gross pay is ' + str(gross_pay))
except ValueError:
    print('invalid input')