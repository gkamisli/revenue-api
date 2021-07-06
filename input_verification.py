from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from datetime import datetime

def get_company_name(branch_id: str):

    id_conv = {'352h67i328fh': 'Sushi',
                '2hg8j32gw8g': 'Taco',
                '345hngydkgs': 'Pizza'}

    if branch_id in id_conv.keys():
        return id_conv[branch_id]
    else:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Invalid branch id. Try correct id.')

def get_date_format(date: str):

    if date[4] == '-' and date[-3] == '-':
        date = datetime.strptime(date, "%Y-%m-%d")
        return date
    else:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Invalid date format. It should be YYYY-MM-DD.')

def get_hourly_dates(date_1: str, date_2: str):

    date_1 = get_date_format(date_1)
    date_2 = get_date_format(date_2)

    if date_1.date() == date_2.date():
        return date_1
    else:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Start date and end date are not the same.')
    
