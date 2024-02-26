# Subject of this python script
# Authored by: Dr.Aammar Tufail
# Where to contact: github profile link "OR" email

# Step-1: Why to use single quotation?
print('Kaleem') # when we are writing a string

# Step-2: When we use """ double quotation marks?
print("kaleem")
print("What's up") # when writing strings and making use of other quoattion marks

# Step-3: when to use '''tripple quotation marks'''?
print('''
      Kaleem's
      Notebook
      ''') # To wrie multiline strings and also use "" or ' quotation marks inside

# Assignments: When to use comments in python? Mention 10 study cases?
# Documentation Strings: Documentation strings provide an official and complete documentation for 
# a function, method, module, or class. This information is important for developers to understand 
# the functionality of the code.
# python
# Copy code
# def add(a, b):
#     """
#     Add two numbers
#     Args:
#         a: First number
#         b: Second number
#     Returns:
#         The sum of the two numbers
#     """
#     return a + b
# Code Complexity: In some cases, complex code might be challenging to understand without additional comments. 
# Adding comments to explain the purpose or functionality of a particular part of the code can help.
# python
# Copy code
# def process_data(data):
#     # Sort the data
#     data.sort()
    
#     # Filter out duplicate values
#     data = list(set(data))
    
#     # Calculate the average value
#     average = sum(data) / len(data)
    
#     return average
# Explaining Intentions: If your code has an alternative approach to achieve a goal, using comments can explain
# your thought process.
# python
# Copy code
# def is_prime(n):
#     """Check if a number is prime"""
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# Bug Fixes: Comments can also be used to document a bug that has been fixed, providing valuable information 
# to future developers.
# python
# Copy code
# def divide(a, b):
#     """
#     Divide two numbers
#     Args:
#         a: First number
#         b: Second number
#     Returns:
#         The result of the division
#     """
#     # This check ensures that we do not encounter a division by zero error
#     if b == 0:
#         return None
#     return a / b
# Removing Dead Code: Comments can be used to indicate dead code, rather than removing it from the source code.
# python
# Copy code
# def add(a, b):
#     # This implementation of addition has been deprecated
#     # return a + b
    
#     # This is the new implementation of addition
#     return a + b
# Third-Party Library Integration: If your code relies on third-party libraries, using comments can provide helpful 
# information about how to use these libraries.
# python
# Copy code
# import pandas as pd

# def read_data(file_path):
#     """
#     Read data from a CSV file
#     Args:
#         file_path: The path to the CSV file
#     Returns:
#         A pandas DataFrame containing the data from the CSV file
#     """
#     # Use the pandas library to read the CSV file
#     data = pd.read_csv(file_path)
    
#     return data
# Commenting Out Code: When debugging, you might comment out sections of code using the # symbol. This way, you can 
# easily uncomment them later when you have resolved the issue.
# python
# Copy code
# def process_data(data):
#     # Remove the duplicate values from the data
#     # data = list(set(data))
    
#     # Sort the data in ascending order
#     data.sort()
    
#     return data
# Linking to Other Parts of the Code: If a function or method relies on another part of the code, adding a comment 
# that links to the specific line or function can be helpful.
# python
# Copy code
# def process_data(data):
#     """
#     Process the data
#     Args:
#         data: The data to be processed
#     Returns:
#         The processed data
#     """
#     # Convert the data to a set to remove duplicate values
#     # Refer to the function 'remove_duplicates' on line 25
#     data = list(set(data))
    
#     # Sort the data in ascending order
#     data.sort()
    
#     return data
# Linking to External Resources: If a function or method relies on external resources like APIs or documentation, 
# adding a comment with a link can be useful.
# python
# Copy code
# def get_weather_data(location):
#     """
#     Get the weather data for a location
#     Args:
#         location: The location for which to retrieve the weather data
#     Returns:
#         The weather data for the specified location
#     """


