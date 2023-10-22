from datetime import datetime, timedelta, date


def get_previous_week_dates(year = datetime.now().year, week_number=1):
    specified_date = datetime.fromisocalendar(year, week_number, 1)
    
    monday_to_friday_dates = []
    monday = specified_date
    friday = monday + timedelta(days=4)
    
    return [monday, friday]
    
    
