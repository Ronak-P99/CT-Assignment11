'''
4. Python Regex Challenge: Enhancing E-Commerce Operations
Objective:

This assignment aims to refine your skills in using Python Regular Expressions to address common challenges in e-commerce operations. 
You will focus on tasks such as product categorization, customer review analysis, and data formatting, 
crucial for efficient e-commerce management.

Task 1: Product Description Keyword Tagging

Problem Statement:
You have a list of product descriptions. Your task is to tag each product based on keywords in the description. 
For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.

Code Example:

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
# Tag each product based on keywords in the description
# Your code here
Expected Outcome:

Convert all price formats in the string to a standardized 'USD XX.XX' format.
Use re.sub() to perform the necessary replacements and format transformations.'''

import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
print("\n")

elec = re.sub(r"\bS\w*e\b", r"Electronics: USD $600.00 \g<0>", descriptions[0])
print(elec)

print("\n")

shirt = re.sub(r"\bC\w*n\b", r"Apparel: USD $24.99 \g<0>", descriptions[1])
print(shirt)

print("\n")

home = re.sub(r"\bS\w*s\b", r"Home & Kitchen: USD $30.00 \g<0>", descriptions[2])
print(home)
print("\n")

