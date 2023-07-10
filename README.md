# Take Home Project

Challenge: A directory contains multiple files and directories of non-uniform file and directory names. Create a program that traverses a base directory and creates an index file that can be used to quickly lookup files by name, size, and content type.

# Usage
To use this script perfectly, follow the steps below:

1. Provide the absolute path to the root directory where the search will be done and assign it to a variable.

Example: 
base_directory = '/Users/agneslamptey/Documents/takehome'

2. Call the function "traverse_directory(base_folder)" and assign it to a variable to run the search in the root folder you provided earlier.

Example:
index = traverse_directory(base_directory)

3. Provide the name of the csv file to be created and assign it to a variable. 
Note: In this case, the name of the csv file should be "index"

Example:
output_file = '../index.csv'

4. Call the function "save_index_to_csv(index, output_file)" that will create and write the search indexes to the csv file you provided earlier.

Example:
save_index_to_csv(index, output_file) 

Output:
A csv file will be created containing all the search indexes as expected.