# Go through files in /Volumes/Tristan_Mac/StockEOD/ChannelUP/ add the ohlccv data if file is less than
# 20 days old, or move to /Volumes/.../ChannelUP/Old if file is 21 or more days old

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
            url = f'https://finance.yahoo.com/quote/{PurePath(d).stem}/history?period1=1626912000&period2=1626998400' \
                  f'&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true '
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
