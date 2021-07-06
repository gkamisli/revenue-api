from fastapi import FastAPI, Query
from db import DB
from input_verification import get_company_name, get_date_format, get_hourly_dates
from starlette.responses import RedirectResponse

app = FastAPI()
db = DB()

@app.get('/', include_in_schema=False)
async def index():
    return RedirectResponse('/docs')


@app.get('/revenue')
async def cust_revenue(branch: str, 
                      start_date: str = Query(None, alias='from', title="Start date", description="Start date for the daily/total revenues"), 
                      end_date: str = Query(None, alias='to', title="End date", description="End date for the daily/total revenues")):
    company_name = get_company_name(branch)
    start_date = get_date_format(start_date)
    end_date = get_date_format(end_date)

    return db.get_revenue(company_name, start_date, end_date)


@app.get('/hourly')
async def cust_hourly_revenue(branch: str, 
                            start_date: str = Query(None, alias='from', title="Start date", description="Start date for the hourly revenues"), 
                            end_date: str = Query(None, alias='to', title="End date", description="End date for the hourly revenues")):
    company_name = get_company_name(branch)
    #date = get_date_format(date)
    date = get_hourly_dates(start_date, end_date)

    return db.get_hourly_rev(company_name, date)
