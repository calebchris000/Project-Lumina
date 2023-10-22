from datetime import datetime, timedelta, date


def get_previous_week_dates():
    current_date = datetime.now()
    previous_friday = current_date - timedelta(days=current_date.weekday() + 3)
    previous_monday = previous_friday - timedelta(days=4)

    return [previous_monday, previous_friday]


# current_date = [
#     date(2023, 1, 2),
#     date(2023, 1, 3),
#     date(2023, 1, 3),
#     date(2023, 1, 4),
#     date(2023, 1, 2),
# ]

# obj = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}


# for each_date in current_date:
#     weekday = each_date.weekday()

#     if weekday in obj:
#         obj[weekday] += 1

# print(obj)
