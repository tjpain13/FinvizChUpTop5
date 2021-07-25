# FinvizChUpTop5


Purpose:

This searches for the top 5 entries in Finviz's "Channel Up" category and then appends open, high, low, close, adjusted close, and volume data (ohlccv) for each entry to a file in a location of your choice. Data is appended to the files if they are less than 20 days old. Files older than 20 days are moved to a directory named ".Old" (note the "."), which is also created if it doesn't exist.

Before Use:

YOU WILL NEED TO define the path variable in Maker.py and Writer.py to signify where you want the program to save files (and the .Old directory). These two locations must be the same. Make sure to include leading and trailing "/" or "\" as necessary. This code has been tested on MacOS with "/", but if the rest of the code works on other OS's (may or may not be true), I think the file path should work with "\" as well.
For example, say the path variable is set to "/My/File/Path/" and the ticker is AAPL (unlikely). The program would save the data to "/My/File/Path/AAPL.json".

Use:

Maker.py will find the current top 5 "Channel Up"s from Finviz.com and then create files corresponding with those entries in a location of your choice. These files  will contain the ticker name and file creation date.
Writer.py will append ohlccv data to each file in the location you choose if it is less than 20 days old or will move the file to a directory named ".Old", which will be created if necessary.
OHLCV_call.py is used in Writer.py but is not intended to be run as a standalone. 
As for actual use, these could be integrated into and run from a main program, or run from a scheduler, or run manually, or who knows what else. I'll leave that up to you.


work in progress - more to come
