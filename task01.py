from datetime import datetime

def get_days_from_today(date):
   try:
       date_object = datetime.strptime(date, "%Y-%m-%d")
       current_date = datetime.today()
       difference_in_days = current_date - date_object
       return difference_in_days.days
   except ValueError:
       return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

print(get_days_from_today("1993-04-01"))   