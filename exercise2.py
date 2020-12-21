"""
Author: Mitchell Lazarz
Creation Date: 23 September 2020
Version: Python 3--Google Colab--Jupytor Notebook
Description:  This script takes a multi-line string of web-scraped weather 
forecast information and cleans the string into a presentable format.  Lines are removed
and commas, colons, and spaces are added for a more readable output.
"""

# -*- coding: utf-8 -*-
# Keep the line above when running script
# Tells python what encoding the string is stored in

# The variable, forecast, is assigned to the scraped multi-line string of weather forecast information 
forecast = '''

Tonight
ClearLow: 55 F

Thursday
Sunny thenChanceShowersHigh: 77 F

Friday
SunnyHigh: 73 F

Saturday
Mostly SunnyHigh: 77 F

Sunday
Mostly SunnyHigh: 71 F
'''

# The forecast string is split into a list using two blank lines (\n\n) as the separator
# A list item is created at every separator
forecast_list = forecast.split('\n\n')

del forecast_list[0]  # Removes empty list in first line of output

# These lines loop through the list while removing blank spaces and adding commas and colons for cleaner display

for day in forecast_list: # For elements in the forecast_list                                             
    day = day.replace('\n',': ') # A line break is replaced by a colon followed by a space
    day = day.replace("Clear","Clear,") # Commas are added at the end of Clear
    day = day.replace("Sunny","Sunny,") # Commas are added at the end of Sunny
    day = day.replace(", thenChanceShowers"," then Chance Showers,") # The comma before thenChanceShowers is removed, spaces are added, along with a comma at end
    day = day.replace("Low", " Low") # A space is added before Low
    day = day.replace("High", " High") # A space is added before High
    day = day.replace("F:","F") # The colon is removed after the temperature unit
    
    print(day) # The weather observations for tonight through Sunday are printed in clean formatting
