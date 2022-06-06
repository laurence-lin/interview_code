import re

from jsonschema import SchemaError


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
            if year < 1901:
                raise ValueError("Start date should be earlier than 01/01/1901")
        else:
            if year > 2999:
                raise ValueError("End date should before 31/12/2999")


def cnt_date_diff(start_dt, end_dt):

    cnt = 0
    str_d, str_m, str_yr = parse_date(start_dt)
    end_d, end_m, end_yr = parse_date(end_dt)

    cnt += (end_yr - str_yr - 1) * 365
    cnt += sum(day_in_month[str_m:]) + (day_in_month[str_m - 1] - str_d)

    cnt += sum(day_in_month[: end_m - 1]) + end_d

    if cnt > 0:
        cnt -= 1

    return abs(cnt)


if __name__ == "__main__":
    print("Please input start date (Format DD/MM/YYYY):")

    start_day = str(input())

    validate_date(start_day, start=True)

    print("Please input end date (Format DD/MM/YYYY):")

    end_day = str(input())

    validate_date(end_day, start=False)

    date_diff = cnt_date_diff(start_day, end_day)
    print("Date difference: ", date_diff)
