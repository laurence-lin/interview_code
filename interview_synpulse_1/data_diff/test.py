from cnt_days import validate_date, cnt_date_diff
import pandas as pd
import os
import sys
from datetime import datetime

#txt_file = "/Users/linyanliang/experiment/interview2022/synpous_dataeng/data_diff"
test_case = sys.argv[1]
print("Read test case from:", test_case)
df = pd.read_csv( test_case, sep=',', header=None)
df.columns = ["start_dt", "end_dt"]

print("This program test the test case in test.txt, and calculate date difference")

for i in range(len(df)):
    print("Start testing case: ", i + 1)
    test_case = df.iloc[i, :]
    start_dt = test_case["start_dt"].strip()
    end_dt = test_case["end_dt"].strip()
    validate_date(start_dt, True)
    validate_date(end_dt, False)

    cnt_diff = cnt_date_diff(start_dt, end_dt)

    start_t = datetime.strptime(start_dt, "%d/%m/%Y")
    end_t = datetime.strptime(end_dt, "%d/%m/%Y")
    date_diff = abs((end_t - start_t).days)
    if date_diff <= 2: # date difference = 0 OR 1, equals 0
        date_diff = 0
    else:
        date_diff -= 1

    print("Start date: {}  End date: {}  Day difference: {} Datetime Library diff: {}".format(start_dt, end_dt, cnt_diff, date_diff))

    # Compare date difference calculated by library

