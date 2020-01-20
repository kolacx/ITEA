from flask import Flask, request
from flask import render_template, redirect
from db_data import STUDENTS

app = Flask(__name__)

@app.route('/students')
def get_students():
    return render_template('students.html', students=STUDENTS)

@app.route('/students/<int:student_id>')
def get_students_marks(student_id):

    student = STUDENTS[student_id]

    return render_template('marks.html', 
                            marks=student['marks'], 
                            average=sum(student['marks']) / len(student['marks']))


@app.route('/students/create', methods=['POST'])
def create_user():

    students_dict = dict(request.form)
    students_dict['marks'] = list(students_dict['marks'])
    STUDENTS.append(dict(students_dict))
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True)