from datetime import date

def date_today():
    day_now = date.today()
    return day_now.strftime('%B %d, %Y')

print(date_today())
