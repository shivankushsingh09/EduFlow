from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# Data storage file
DATA_FILE = '/app/data/students.json'

def load_students():
    """Load students data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    """Save students data to JSON file"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)

@app.route('/')
def index():
    """Home page - Dashboard"""
    students = load_students()
    total_students = len(students)
    active_students = len([s for s in students if s.get('status', 'active') == 'active'])
    return render_template('index.html', students=students, total_students=total_students, active_students=active_students)

@app.route('/students')
def students():
    """Students list page"""
    students = load_students()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    """Add new student"""
    if request.method == 'POST':
        students = load_students()
        new_student = {
            'id': len(students) + 1,
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'course': request.form['course'],
            'enrollment_date': datetime.now().strftime('%Y-%m-%d'),
            'status': 'active'
        }
        students.append(new_student)
        save_students(students)
        return redirect(url_for('students'))
    return render_template('add_student.html')

@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    """Edit student information"""
    students = load_students()
    student = next((s for s in students if s['id'] == student_id), None)
    
    if not student:
        return "Student not found", 404
    
    if request.method == 'POST':
        student['name'] = request.form['name']
        student['email'] = request.form['email']
        student['phone'] = request.form['phone']
        student['course'] = request.form['course']
        student['status'] = request.form['status']
        save_students(students)
        return redirect(url_for('students'))
    
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:student_id>')
def delete_student(student_id):
    """Delete student"""
    students = load_students()
    students = [s for s in students if s['id'] != student_id]
    save_students(students)
    return redirect(url_for('students'))

@app.route('/api/students')
def api_students():
    """API endpoint to get students data"""
    students = load_students()
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
