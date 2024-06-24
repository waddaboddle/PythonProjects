def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_input, month_input):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year_input < 0:
        return "Invalid year"
    if 1 > month_input > 12:
        return "Invalid month"
    if not is_leap(year_input):
        month_days = month_days[month_input - 1]
    else:
        month_days = leap_month_days[month_input - 1]
    return month_days


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
