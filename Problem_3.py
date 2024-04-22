'''
3. Advanced Text Processing with Python Regex
Objective:
The goal of this assignment is to harness the full potential of Python's Regular Expressions for advanced text processing. 
You'll tackle complex tasks involving data extraction, validation, and transformation, 
sharpening your skills in applying regex in various challenging scenarios.

Task 1: Advanced Data Extraction

Problem Statement:
Develop a script to extract specific information from a formatted text. 
The text contains data entries delimited by semicolons and formatted as 'Key: Value'. Extract the value corresponding to a specific key.

Code Example:

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
# Your code here

Expected Outcome:

Correctly identify and categorize valid and invalid URLs from the list.
Use regex to validate the format of each URL.'''

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
# Your code here

occupation = re.findall(r"\bE\w*r\b", text)
print(f"The occupation we end up getting is {occupation}")