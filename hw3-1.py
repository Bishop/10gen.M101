import pymongo

connection = pymongo.Connection('localhost', safe=True)

students = connection.school.students

for student in students.find():
    low_value = None
    for score in student['scores']:
        if score['type'] == 'homework':
            low_value = score['score'] if low_value is None else min(score['score'], low_value)
    
    students.update({'_id': student['_id']}, {'$pull': {'scores': {'type': 'homework', 'score': low_value}}})