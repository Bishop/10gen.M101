import pymongo

from pymongo import Connection
connection = Connection('localhost')

grades = connection.students.grades

sorted_scores = grades.find().sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

student_id = None

for row in sorted_scores:
    if student_id != row['student_id']:
        student_id = row['student_id']
        grades.remove(row)