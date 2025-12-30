from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eduflow_secret_key_2024'

# Database configuration - support both local and Docker environments
if os.environ.get('DOCKER_ENV'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/eduflow.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduflow.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    course = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    
    grades = db.relationship('Grade', backref='student', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Student {self.name}>'

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    
    grades = db.relationship('Grade', backref='course', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Course {self.code}>'

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Grade {self.grade}>'

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    all_students = Student.query.order_by(Student.enrollment_date.desc()).all()
    return render_template('students.html', students=all_students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    return add_student_handler()

@app.route('/add_student', methods=['GET', 'POST'])
def add_student_alt():
    return add_student_handler()

def add_student_handler():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        course = request.form.get('course')
        semester = request.form.get('semester')
        
        if not all([name, email, phone, course, semester]):
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_student'))
        
        try:
            student = Student(
                name=name,
                email=email,
                phone=phone,
                course=course,
                semester=int(semester)
            )
            db.session.add(student)
            db.session.commit()
            flash('Student added successfully!', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            flash(f'Error adding student: {str(e)}', 'danger')
            return redirect(url_for('add_student'))
    
    return render_template('add_student.html')

@app.route('/students/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    
    if request.method == 'POST':
        student.name = request.form.get('name')
        student.email = request.form.get('email')
        student.phone = request.form.get('phone')
        student.course = request.form.get('course')
        student.semester = int(request.form.get('semester'))
        
        try:
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            flash(f'Error updating student: {str(e)}', 'danger')
            return redirect(url_for('edit_student', id=id))
    
    return render_template('edit_student.html', student=student)

@app.route('/students/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting student: {str(e)}', 'danger')
    
    return redirect(url_for('students'))

@app.route('/courses')
def courses():
    all_courses = Course.query.all()
    return render_template('courses.html', courses=all_courses)

@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        credits = request.form.get('credits')
        instructor = request.form.get('instructor')
        
        if not all([name, code, credits, instructor]):
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_course'))
        
        try:
            course = Course(
                name=name,
                code=code,
                credits=int(credits),
                instructor=instructor
            )
            db.session.add(course)
            db.session.commit()
            flash('Course added successfully!', 'success')
            return redirect(url_for('courses'))
        except Exception as e:
            flash(f'Error adding course: {str(e)}', 'danger')
            return redirect(url_for('add_course'))
    
    return render_template('add_course.html')

@app.route('/grades')
def grades():
    all_grades = Grade.query.order_by(Grade.created_at.desc()).all()
    return render_template('grades.html', grades=all_grades)

@app.route('/grades/add', methods=['GET', 'POST'])
def add_grade():
    students = Student.query.all()
    courses = Course.query.all()
    
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')
        grade = request.form.get('grade')
        semester = request.form.get('semester')
        
        if not all([student_id, course_id, grade, semester]):
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_grade'))
        
        try:
            new_grade = Grade(
                student_id=int(student_id),
                course_id=int(course_id),
                grade=grade,
                semester=int(semester)
            )
            db.session.add(new_grade)
            db.session.commit()
            flash('Grade added successfully!', 'success')
            return redirect(url_for('grades'))
        except Exception as e:
            flash(f'Error adding grade: {str(e)}', 'danger')
            return redirect(url_for('add_grade'))
    
    return render_template('add_grade.html', students=students, courses=courses)

@app.route('/api/students')
def api_students():
    students = Student.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'email': s.email,
        'phone': s.phone,
        'course': s.course,
        'semester': s.semester
    } for s in students])

if __name__ == '__main__':
    with app.app_context():
        # Create data directory if it doesn't exist (for Docker)
        if os.environ.get('DOCKER_ENV') and not os.path.exists('data'):
            os.makedirs('data')
        db.create_all()
    
    # Support both local development and Docker deployment
    host = '0.0.0.0' if os.environ.get('DOCKER_ENV') else '127.0.0.1'
    app.run(debug=not os.environ.get('DOCKER_ENV'), host=host, port=5000)
