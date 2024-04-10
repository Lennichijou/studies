from datetime import datetime
import re


def closest_date(*dates: tuple) -> str:
    datetime_list = [datetime.strptime(date, "%d.%m.%Y") for date in dates]
    today = datetime.today()
    date_diffs = [abs(date - today) for date in datetime_list]
    return dates[date_diffs.index(min(date_diffs))]


date_list, n, i = [], int(input()), 0
while i != n:
    entered_date = input()
    if re.fullmatch("\d\d.\d\d.\d{4}", entered_date):
        date_list.append(entered_date)
        i += 1
    else:
        print("Повторите ввод.")

print(closest_date(*date_list))
