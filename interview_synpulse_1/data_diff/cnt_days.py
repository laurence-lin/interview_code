import re

from jsonschema import SchemaError
from test_leap import is_leap, get_order_date

# Examine:
# end date < start date
# date not in 01/01/1901 & 31/12/2999

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



def parse_date(date):
    day, month, year = map(lambda val: int(val), date.split("/"))
    return day, month, year


def validate_date(date, start=False):
    if not re.match(r"\d\d\/\d\d\/\d\d\d\d", date):
        raise ValueError("Input date is invalid in format! Please input in format DD/MM/YYYY")

    else:
        day, month, year = parse_date(date)
        if day <= 0 or month <= 0 or year <= 0:
            raise ValueError("Date value should be positive")
        if month == 2 and day > 29:
            raise ValueError("Day value invalid for Februrary")
        elif month > 12 or day > 31:
            raise ValueError("Month and Day value is invalid")

        if start:
            if year < 1901 or year > 2999:
                raise ValueError("The data should be located between 01/01/1901 - 31/12/2999")
        else:
            if year < 1901 or year > 2999:
                raise ValueError("The data should be located between 01/01/1901 - 31/12/2999")


def cnt_date_diff(start_dt, end_dt):
    # Consider leap year: in leap year, days per year = 366
    cnt = 0

    (str_d, str_m, str_yr), (end_d, end_m, end_yr) = get_order_date(start_dt, end_dt) 

    if abs(end_yr - str_yr) > 0:
       year_is_leap = list(map(lambda yr: is_leap(yr), range(str_yr, end_yr+1))) # [True, False, ....] referring is_leap year or not
       year_list_days = [366 if val else 365 for val in year_is_leap]  # [365, 366, ...]
    
    else:
        year_is_leap = []
        year_list_days = []


    if year_is_leap: # If start year and end year is not same
        print("Days in interval year:", sum(year_list_days[1:-1]))
        cnt += sum(year_list_days[1:-1]) # 1. days in interval year
        # 2. days in start year
        print("Days in start year:",  ( sum(day_in_month[str_m:]) + (day_in_month[str_m - 1] - str_d) ))
        cnt += ( sum(day_in_month[str_m:]) # days of rest of month
            + (day_in_month[str_m - 1] - str_d) ) # days from start month to end of the start month
        if year_is_leap[0]: # if start year is leap year
            day_in_month[1] = 29

        if year_is_leap[-1]:
            day_in_month[1] = 29
        else:
            day_in_month[1] = 28

        print("Days in end year:", sum(day_in_month[: end_m - 1]) + end_d - 1)
        cnt += sum(day_in_month[: end_m - 1]) + end_d - 1  # 3. days in end year

    else: # start year = end year
        # start month = end month
        if str_m == end_m:
            cnt += (end_d - str_d - 1)

        else: # end month > start month
            print("start month:", ( (day_in_month[str_m - 1] - str_d)))
            print("interval month:", sum(day_in_month[str_m:end_m]) )
            print("End day:", end_d)
            cnt += ( (day_in_month[str_m - 1] - str_d) # days from start month to end of start month
             + sum(day_in_month[str_m:end_m-1]) # days in interval month
             +  end_d) - 1 # substract the end day

    return abs(cnt)


if __name__ == "__main__":
    print("Please input start date (Format DD/MM/YYYY):")
    print("The data should be located between 01/01/1901 - 31/12/2999, otherwise invalid")

    start_day = str(input())

    validate_date(start_day, start=True)

    print("Please input end date (Format DD/MM/YYYY):")

    end_day = str(input())

    validate_date(end_day, start=False)

    date_diff = cnt_date_diff(start_day, end_day)
    print("Date difference: ", date_diff)
