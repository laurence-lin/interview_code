from cnt_days import validate_date, cnt_date_diff
import pandas as pd
import os

#txt_file = "/Users/linyanliang/experiment/interview2022/synpous_dataeng/data_diff"
df = pd.read_csv( "test.txt", sep=',', header=None)
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
    print("Start date: {}  End date: {}  Day difference: {}".format(start_dt, end_dt, cnt_diff))
