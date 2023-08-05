from datetime import datetime, timedelta

def datetime_logic():
    fileHeader = datetime.now().strftime('%Y-%m-%d')
    print(fileHeader)

    date = datetime.strptime('2021/07-06', '%Y/%m-%d')
    print(date)
    print(date.strftime('%Y-%m-%d'))

    date.replace(year=2020)
    
def datetime_arithematic():
    date = datetime.strptime('2021/07-06', '%Y/%m-%d')
    print(date)

    date1 = date + timedelta(days=1, hours=12, minutes=30, seconds=30, microseconds=30, milliseconds=30)
    print(date1)

    date2 = date - timedelta(days=1, hours=12, minutes=30, seconds=30, microseconds=30, milliseconds=30)
    print(date2)
    
    print((date1 - date2).days)
    
datetime_arithematic()