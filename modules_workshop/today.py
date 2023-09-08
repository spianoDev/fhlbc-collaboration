import datetime

# Create a function to print the date with September 8, 2023
def today_is():
    todays_date = datetime.date.today()
    return todays_date.strftime('%B %d, %Y')

print(today_is())
