from datetime import datetime, timedelta, date
import calendar

def get_week_dates(year = datetime.now().year, week_number=1):
    specified_date = datetime.fromisocalendar(year, week_number, 1)
    
    monday = specified_date
    friday = monday + timedelta(days=4)
    
    return [monday, friday]


def get_monthly_dates(year = datetime.now().year, month: int = 1):
    specified_date = datetime.now()
    

def run(year: int = 2023, month: int=10):
    specified_date = date(year=year, month=month, day=1)
    return specified_date

