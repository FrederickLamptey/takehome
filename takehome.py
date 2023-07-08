import os    #importing os module into the code to be able to interact with the operating system of the computer
import mimetypes  #importing mimetypes module into the code in order to map filenames/URL to their corresponding MIME type
import csv  #importing csv to help work with comma separated values files (CSV)


def traverse_directory(base_folder):
    '''
    a function that will search/iterate through the base directory, and all the files in it, and return them as a list called index
    '''
    index = [] #empty list that will store the data or content of base directory
    for root, dirs, files in os.walk(base_folder):  #for loop to iterate or go through the base directory that would outcome a tuple(root,dir,files)
        for file in files: #for loop to iterate each file in the files in the base directory
            file_path = os.path.join(root, file)  #joining each iterated file to the root file path and assigning it to the variable file_path
            file_name = os.path.basename(file_path)  #extracting the filename from each file path created/joined above, and assigning it to file_name
            file_size = os.path.getsize(file_path)  #retrieving the size of each file(bytes) and assigning it to file_size
            file_content_type, _ = mimetypes.guess_type(file_path) #assigning MIME type of each file to file_content_type based on their ext.
            index.append({'Name': file_name, 'Size': file_size, 'Content Type': file_content_type}) #adding each file with its corresponding info to the list.
    return index #returning the list to be able to be stored under a variable.

def save_index_to_csv(index, output_file):
    '''
    This function will save the index returned from function traverse_directory(base_folder) to a CSV file
    '''
    fieldnames = ['Name', 'Size', 'Content Type'] #assigning a list containing column names to be used in the csv file to the variable fieldnames
    with open(output_file, 'w', newline='') as csvfile: #opening the file(output_file) in "write" mode with default newline handling
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #writes a row of data using the fieldnames(columns) based on dictionary
        writer.writeheader() #writes the header from the "writer"
        writer.writerows(index) #writes the content of the list returned from the function traverse_directory(base_folder) to the csvfile.

# Calling/running script
base_directory = '/Users/agneslamptey/Documents/takehome'
index = traverse_directory(base_directory)
output_file = '../index.csv'
save_index_to_csv(index, output_file)

'''
base_directory = '/Users/agneslamptey/Documents/takehome'
index = traverse_directory(base_directory)
current_directory = os.getcwd()
output_file = os.path.join(current_directory, 'index.csv')
save_index_to_csv(index, output_file)
'''