import datetime

day = int(input("Enter the day of birth (e.g., 14): "))
month = int(input("Enter the month of birth (e.g., 12 for December): "))
year = int(input("Enter the year of birth (e.g., 2008): "))

birth_date = datetime.date(year, month, day)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week = days_of_week[birth_date.weekday()]

current_date = datetime.date.today()
age_in_days = (current_date - birth_date).days

print(f"You were born on a {day_of_week}.")
print(f"You are {age_in_days} days old.")