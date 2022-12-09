""" 
Final Python Project
Emran A., Sami S., Dagmawe A. 
Assignment Final Python Project
Date: 11/29/2022
INST326-ESG1 Farmer Fall 2022
"""

# Import the csv and argparse modules
import csv
import argparse

# Define a function to parse the command-line arguments
def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--csv', required=True, help= 'Path to the CSV file containing the classes')
  parser.add_argument('--semesters', type=int, required=True, help= 'Number of semesters to generate a course plan for')
  parser.add_argument('--output', help= 'Path to the output file where the course plan will be saved')
  return parser.parse_args()

# Define a function to read the classes from the CSV file
def read_classes(csv_file):
  # Initialize an empty dictionary to store the classes
  classes = {}

  # Open the CSV file and create a reader object to read the data
  with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    # Loop through the rows of the CSV file
    for row in reader:
      # Get the semester and class name from the row
      semester = row[0]
      class_name = row[1]

      # Check if the semester exists in the dictionary
      if semester not in classes:
        # If the semester does not exist, add it to the dictionary
        classes[semester] = []


