""" 
Final Python Project
Emran A., Sami S., Dagmawe A. 
Assignment Final Python Project
Date: 11/29/2022
INST326-ESG1 Farmer Fall 2022
"""

import csv
import argparse

'''Student class creates a student with 1 attribute: credits'''
class Student:

  def __init__(self,credits):
    self.credits = credits


'''Function to read the courses from CSV file'''
def read_classes(input_file):
  classes = {}

  with open(input_file, 'r') as file:
    reader = csv.reader(file)

    for row in reader:

      semester = row[0]
      class_name = row[1]

      if semester not in classes:
        classes[semester] = []

      classes[semester].append(class_name)

  return classes

''' Function creates the course plan with attributes: semesters, classes '''
def create_plan(semesters, classes):

  plan = []

  for semester in range(1, semesters+1):

    if semester in classes:
      plan.extend(classes[semester])

    else:
      plan.append('')

  return plan

'''Define a function to parse the command-line arguments'''
def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', required= True, help= 'Path to the CSV file containing the classes')
  parser.add_argument('--semesters', type= int, required= True, help= 'Number of semesters to generate a course plan for')
  parser.add_argument('--output', help= 'Path to the output file where the course plan will be saved')
  return parser.parse_args()

def main():

  args = parse_args()
  classes = read_classes