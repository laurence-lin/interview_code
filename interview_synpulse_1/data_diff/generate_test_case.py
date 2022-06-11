from datetime import datetime, date, timedelta
import random


def get_random_str_end_date():
    str_date = date(random.randint(1901, 2000), random.randint(1, 12), random.randint(1, 28))
    end_date = str_date + timedelta(days=random.randint(100, 5000))

    str_date = datetime.strftime(str_date, "%d/%m/%Y")
    end_date = datetime.strftime(end_date, "%d/%m/%Y")

    return str_date, end_date

N_TEST = 20

with open("test_new.txt", "w") as file:
    for i in range(N_TEST):
        str_, end_ = get_random_str_end_date()
        test_case = ",".join([str_, end_])
        file.write(test_case + "\n")









