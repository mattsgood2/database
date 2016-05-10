from peewee import *

sqlite_db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = sqlite_db

students = [
    {'username': 'Matthew Goodman',
     'points': 2000},
    {'username': 'Pim Goodman',
     'points': 2001},
    {'username': 'Jessica Goodman',
     'points': 1900},
    {'username': 'Leo Goodman',
     'points': 1800},
    {'username': 'Lillie Goodman',
     'points': 1500},
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':
    sqlite_db.connect()
    sqlite_db.create_tables([Student], safe=True)
    add_students()
    print('Our Top Student is {0.username}'.format(top_student()))
