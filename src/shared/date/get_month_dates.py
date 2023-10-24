from datetime import datetime, date, timedelta
import pytz

def get_monday_friday_pairs(
    year: int = date.today().year, month: int = date.today().month
):
    timezone = pytz.timezone("Europe/Paris")
    
    start_date = datetime(year=year, month=month, day=1, tzinfo=timezone)
    date_pairs = []
    
    #* Edge cases to constrain Monday - Friday on the specified month  
    # if 1 <= start_date.weekday() <= 4:
    #     while start_date.weekday() != 4:
    #         start_date += timedelta(days=1)
    #     date_pairs.append([start_date.strftime('%Y-%m-%d')])


    while start_date.weekday() != 0:
        start_date += timedelta(days=1)

    while start_date.month == month:
        end_date = start_date

        while end_date.weekday() != 4:
            end_date += timedelta(days=1)

        date_pairs.append(
            [start_date, end_date]
        )
        start_date += timedelta(days=7)

    return date_pairs

