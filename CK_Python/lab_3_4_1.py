from datetime import datetime

date_list = [input() for i in range(int(input()))]


def closest_date(*dates):
    datetime_list = [datetime.strptime(date, "%d.%m.%Y") for date in dates]
    today = datetime.today()
    date_diffs = [abs(date - today) for date in datetime_list]
    return dates[date_diffs.index(min(date_diffs))]


print(closest_date(*date_list))
