from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET' :
		return render_template('add.html')
	else:
		return render_template('student.html',
			student_name = request.form['student_name'],
            student_year = request.form['student_year']
		)



def add_student_info(student_name, student_year):
    Student_object = Student(name=student_name, year=student_year)
    session.add(Student_object)
    session.commit()

def get_all_student_info():
    all_info = session.query(Student).all()
    return all_info



@app.route('/results')
def all_results():
    all_info = get_all_student_info()
    return render_template('student.html', all_responses=all_info)

app.run(debug=True)
