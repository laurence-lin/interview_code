
#year = int(sys.argv[1])
#print("test year:", year)

def parse_date(date):
    day, month, year = map(lambda val: int(val), date.split("/"))
    return day, month, year

def is_leap(year):
    if year%4 != 0:
        return False

    else:
        if year %100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            
            else:
                return True

def get_order_date(date_1, date_2):
    # given start date and end date, return sorted order date with min_date, max_date
    d1, m1, y1 = parse_date(date_1)
    d2, m2, y2 = parse_date(date_2)
    min_date = None
    max_date = None
    reverse = False

    if y1 >= y2:
        if y1 == y2:  # same year
           if m1 > m2: # month 1 > month 2, reverse
               reverse = True
           elif m1 == m2:  # same month
               if d1 > d2:  # date 1 > date 2, reverse
                   reverse = True

        else: # if year 1 > year 2, reverse
            reverse = True

    if reverse:
       min_date = (d2, m2, y2)
       max_date = (d1, m1, y1)
       return min_date, max_date

    else:
       min_date = (d1, m1, y1)
       max_date = (d2, m2, y2)
       return min_date, max_date

