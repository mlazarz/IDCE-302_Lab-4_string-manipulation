# Lab 4 – String Manipulation

This repository contains three scripts that perform elements of string manipulation:

**Script 1**--A function capitalizes the first and fourth letters of the name "macdonald".

**Script 2**--Weather data for Worcester, MA is scraped from the National Weather Service webpage and the extracted data is edited for cleaner presentation.

**Script 3**--The latitude and longitude is extracted from a Google Maps url and is printed.

## The Code

### Script 1

1. A function, called old_macdonald is created called that takes a name as the parameter.
2. The first three letters of the name are sliced out and capitalized; then assigned the variable, prefix.
3. The remainder of the name is sliced out and capitalized; then assigned the variable, suffix.
4. The prefix and suffix are then concantenated and printed.
5. The function is called with the input name, macdonald.


### Script 2

1. A variable, forecast, is assigned to a multi-line string of webscraped weather information for Worcester, MA from the National Weather Service.
2. The multi-line string is then converted to a list by creating a new element at every instance of a double line break.
3. The new list of weather information is looped through and changes are made by using the .replace module.  In this for loop, colons, commas, and spaces are added and removed for a cleaner presentation.
4. After every iteration of the list, a list element is printed to display an output of the weather information for each day of the five day forecast.

*The following is the output of this script:*

Tonight: Clear, Low: 55 F

Thursday: Sunny then Chance Showers, High: 77 F

Friday: Sunny, High: 73 F

Saturday: Mostly Sunny, High: 77 F

Sunday: Mostly Sunny, High: 71 F 



**Code issues:**  The loop iterations used 7 lines of .replace modules.  I wanted to reduce the number of lines while making the code more repeatable for any webscraped forecast.  I would have liked to do this by first replacing new lines with colons then removing all spaces.  Then with an if statement, add spaces back at every instance of a colon or upper case character.  I attempted to add a for loop within the current for loop, but did not have any success.

### Script 3

1. The Google Maps url was assigned a variable, url.
2. The url was then converted into a list by seperating elements by each instance of a backspace.
3. The coordinates within the url are located in index 4, so they were assigned a variable, coordinates.
4. The coordinates string was then converted into a list by seperating elements by each instance of a comma.
5. The latitude and longitude were then able to be extracted through indexing and printed.


*The following is the input and output of this script:*

**Input:** 

url="https://www.google.com/maps/@42.2509428,-71.8249939,17z"

**Output:**  

Latitude: 42.2509428  

Longitude: -71.8249939


