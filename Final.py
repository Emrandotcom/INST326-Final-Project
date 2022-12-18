""" 
Final Python Project
Emran A., Sami S., Dagmawe A. 
Assignment Final Python Project
Date: 11/29/2022
INST326-ESG1 Farmer Fall 2022
"""

import csv
import argparse
import sys

'''Student class creates a student with 1 attribute: credits'''
class Student:

  def __init__(self,credits):

    self.credits = credits

""" Function reads the courses from a CSV file and returns them as a list of lists"""
def read_courses_from_csv(csv_file_name):

    courses = []

    with open(csv_file_name, 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:

            courses.append(row)

    return courses

""" Function calculates the number of credits to take per semester"""
def calculate_semester_credits(total_credits, num_semesters):

    return total_credits // num_semesters

""" Function creates a semester plan by adding courses to the appropriate semester based on credits"""
def create_semester_plan(courses, semester_credits):

    semesters = []

    for course in courses:

        credits = int(course[1])

        most_available_semester = None
        most_available_credits = 0

        for semester in semesters:

            if semester['credits'] > most_available_credits:

                most_available_semester = semester
                most_available_credits = semester['credits']

        if most_available_credits >= credits:

            most_available_semester['courses'].append(course[0])
            most_available_semester['credits'] -= credits

        else:

            semesters.append({'courses': [course[0]], 'credits': semester_credits - credits})
    
    return semesters

""" Function prints the semester plan"""
def print_semester_plan(semesters):

    for i, semester in enumerate(semesters):

        print(f"Semester {i+1}:")

        for course in semester['courses']:

            print(f" - {course}")

def main(csv_file, transfer_credits):

    courses = read_courses_from_csv(csv_file)
    student = Student(transfer_credits)
    total_credits = 120 - student.credits
    semester_credits = calculate_semester_credits(total_credits, 4)
    semesters = create_semester_plan(courses, semester_credits)
    print_semester_plan(semesters)

"""Parses the command line arguments"""
def parse_args(args_list):

    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', help='the CSV file containing the list of courses')
    parser.add_argument('transfer_credits', type=int, help='the number of credits being transferred in')
    return parser.parse_args(args_list)

if __name__ == '__main__':

    args = parse_args(sys.argv[1:])
    main(args.csv_file, args.transfer_credits)