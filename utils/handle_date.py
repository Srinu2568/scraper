import datetime as dt

def handle_date(s):
    months = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
    date_parts = s.split()
    month = date_parts[0].upper()
    if month in months.keys():
        month = months[month]
    else:
        return str(dt.datetime.now().date().day) + '-' + str(dt.datetime.now().date().month) + '-' + str(dt.datetime.now().date().year)
    date = date_parts[1]
    full_date = str(date) + '-' + str(month) + '-' + str(dt.datetime.now().year)
    return full_date
