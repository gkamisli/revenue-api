import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from collections import defaultdict
import json

class DB(object):

    def __init__(self):
        self.df = pd.read_csv('data.csv', low_memory=False)
        self.df['Finalized Date'] = pd.to_datetime(self.df['Finalized Date'],format="%d/%m/%y %H:%M") 
        self.df['Finalized Day'] = [t.date() for t in self.df['Finalized Date']]
        self.df['Finalized Time'] = [t.hour for t in self.df['Finalized Date']]

    def get_revenue(self, company_name, start_date, end_date):

        total_rev = self._get_total_rev(company_name, start_date, end_date)
        daily_rev = self._get_daily_rev(company_name, start_date, end_date)

        result = {
            'from': start_date.strftime("%Y-%m-%d"),
            'to': end_date.strftime("%Y-%m-%d"),
            'total revenue': total_rev,
            'daily revenue': daily_rev}

        return result

    def get_hourly_rev(self, company_name, day):
        day = day.date()
        start_time = datetime.strptime("00:00", "%H:%M")
        end_time = datetime.strptime("23:59", "%H:%M")

        hourly_rev = defaultdict(list)
        delta = timedelta(hours=1)

        while start_time <= end_time:
            mask = (self.df['Company Name'] == company_name) & (self.df['Finalized Day'] == day) & (self.df['Finalized Time'] == start_time.hour)
            hourly_rev[start_time.strftime("%H:%M")+"-"+(start_time+delta).strftime("%H:%M")].append(round(sum(self.df.loc[mask, 'Total'].values), 2) if any(mask) else 'NA')
            start_time += delta

        hourly_rev = {k:v[0] for k,v in hourly_rev.items() if v[0] != 'NA'}
    
        return json.dumps({
            'date': day.strftime("%Y-%m-%d"),
            'hourly revenue': hourly_rev})

    def _get_total_rev(self, company_name, start_date, end_date):
        mask = (self.df['Company Name'] == company_name) & (self.df['Finalized Date'] >= start_date) & (self.df['Finalized Date'] <= end_date)
        total_rev = round(sum(self.df.loc[mask,'Total'].values), 3) if any(mask) else 'No revenue'
        
        return total_rev

    def _get_daily_rev(self, company_name, start_date, end_date):
        start_day = start_date.date()
        end_day = end_date.date()

        daily_rev = defaultdict(list)

        delta = timedelta(days=1)

        while start_day < end_day:
            mask = (self.df['Company Name'] == company_name) & (self.df['Finalized Day'] == start_day)
            daily_rev[start_day.strftime("%Y-%m-%d")].append(round(sum(self.df.loc[mask, 'Total'].values), 2) if any(mask) else 'NA')
            start_day += delta

        daily_rev = {k:v[0] for k,v in daily_rev.items() if v[0] != 'NA'}
    
        return json.dumps(daily_rev)