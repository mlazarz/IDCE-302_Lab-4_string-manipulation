"""
Author:  Mitchell Lazarz
Creation Date:  23 September 2020
Version:  Python 3--Google Colab--Jupytor Notebook
Description:  This code extracts the latitude and longitude from the Google maps
url, https://www.google.com/maps/@42.2509428,-71.8249939,17z.  The output prints 
the latitude and longitude found in the url in a readable format.
"""

url="https://www.google.com/maps/@42.2509428,-71.8249939,17z"  # Google maps link is assigned to variable url
url=url.split("/")                                             # url is converted to list with backspaces as a seperator
coordinates=url[4]                                             # A variable, coordinates, is assigned to the 4th index of url list
coordinates=coordinates.split(",")                             # The string variable, coordinates, is converted to a list with commas as the seperator
lat=coordinates[0][1:]                                         # A variable, lat, is assigned the 0 index of the coordinates list while removing the @ symbol at the beginning of the element
lon=coordinates[1]                                             # A varibale, long, is assigned the first index of the coordinates list

print("Latitude:", lat)                                        # The extracted latitude is printed
print("Longitude:", lon)                                       # The extracted longitude is printed
