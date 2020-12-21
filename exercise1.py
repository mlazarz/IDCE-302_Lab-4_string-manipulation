"""
Author: Mitchell Lazarz
Creation Date: 23 September 2020
Version: Python 3--Google Colab--Jupytor Notebook
Description:  A function is created to capitalize the first and fourth letter
of a name.  In this code, 'macdonald' is modified to be printed as 'MacDonald'.
"""

# Define function that capitalizes the first and fourth letter of a name
def old_macdonald(name):
  prefix=name[:3].capitalize()    # Slices out the first three letters of name and capitalizes the first letter of the segment
  suffix=name[3:].capitalize()    # Slices out letters after the 3rd letter and capitalizes the first letter of the segment
  namecorrection=prefix+suffix    # The two string segments with correct capitalization are concatenated
  print(namecorrection)           # The recombined name is printed
old_macdonald("macdonald")        # Function is called with the name "macdonald"
