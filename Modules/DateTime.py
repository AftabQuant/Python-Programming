import datetime
x = datetime.datetime.now()
print(x)

y = datetime.datetime.date(x)
print(y)

# Print Day
print(x.strftime("%A"))

# Print Month
print(x.strftime("%B"))

# Print Year
print(x.strftime("%Y"))