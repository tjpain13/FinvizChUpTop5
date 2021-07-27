# Go through files in /Your/Path/Here/ add the ohlccv data if file is less than
# 21 days old, or move to /Your/Path/Here/.Old if file is 21 or more days old

import linecache
import os
import datetime
from OHLCV_Call import ohlccv_output
from pathlib import PurePath
from shutil import move


curdt = datetime.date.today()
path = "/Your/Path/Here/"  # add your desired path here, INCLUDE trailing "/" or "\"

for d in os.listdir(f'{path}'):
    if not d.startswith('.'):
        secondline = linecache.getline(f'{path}{d}', 2).rstrip('\n')
        oldday = datetime.datetime.strptime(secondline, "%Y-%m-%d").date()
        dayselapsed = curdt - oldday
        if dayselapsed < datetime.timedelta(days=21):
            url = f'https://finance.yahoo.com/quote/{PurePath(d).stem}/history?p={PurePath(d).stem}'
            stockfile = open(f'{path}{d}', 'a')
            stockfile.write(f'\n{ohlccv_output(url)}')
            stockfile.close()
        elif dayselapsed >= datetime.timedelta(days=21):
            if os.path.isdir(f'{path}.Old') is True:
                move(f'{path}{d}', f'{path}.Old')
            elif os.path.isdir(f'{path}.Old') is False:
                os.mkdir(f'{path}.Old')
                move(f'{path}{d}', f'{path}.Old')
        linecache.clearcache()
