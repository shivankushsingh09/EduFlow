# EduFlow - Student Management System

A comprehensive student management system built with Flask, HTML, CSS, JavaScript, and Bootstrap. This system allows educational institutions to manage students, courses, and grades efficiently.

## Features

### 🎓 Student Management
- Add, edit, and delete students
- Track student enrollment information
- Search and filter students by course and semester
- View student statistics and analytics

### 📚 Course Management
- Create and manage courses
- Assign instructors to courses
- Track course credits and codes
- View course statistics

### 📊 Grade Management
- Add and manage student grades
- Track grade distribution
- View grade statistics and analytics
- Support for various grade scales (A+ to F)

### 🎨 Modern UI/UX
- Responsive Bootstrap 5 design
- Interactive JavaScript features
- Clean and intuitive interface
- Mobile-friendly design

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (with SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd "EduFlow - Student Management System"
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```
   
   **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

### Getting Started

1. **Start the application** by running `python app.py`
2. **Open your browser** and go to `http://localhost:5000`
3. **Explore the dashboard** to see system features
4. **Add your first student** using the "Add Student" button
5. **Create courses** to organize your curriculum
6. **Add grades** to track student performance

### Main Features

#### Home Dashboard
- Overview of system statistics
- Quick access to all main features
- Modern, welcoming interface

#### Student Management
- View all students in a searchable table
- Add new students with complete information
- Edit existing student details
- Delete students (with confirmation)
- Filter by course and semester

#### Course Management
- View all courses in a card layout
- Add new courses with instructor assignment
- Track course credits and codes
- View course statistics

#### Grade Management
- Add grades for students in specific courses
- View grade distribution and statistics
- Color-coded grade badges
- Comprehensive grade analytics

## Project Structure

```
EduFlow - Student Management System/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── index.html        # Home dashboard
    ├── students.html     # Student management page
    ├── add_student.html  # Add student form
    ├── edit_student.html # Edit student form
    ├── courses.html      # Course management page
    ├── add_course.html   # Add course form
    ├── grades.html       # Grade management page
    └── add_grade.html    # Add grade form
```

## Database Schema

The system uses SQLite with the following tables:

- **Students**: Student information (name, email, phone, course, semester)
- **Courses**: Course details (name, code, credits, instructor)
- **Grades**: Grade records (student_id, course_id, grade, semester)

## API Endpoints

The application provides the following main routes:

- `/` - Home dashboard
- `/students` - Student management
- `/students/add` - Add new student
- `/students/edit/<id>` - Edit student
- `/students/delete/<id>` - Delete student
- `/courses` - Course management
- `/courses/add` - Add new course
- `/grades` - Grade management
- `/grades/add` - Add new grade
- `/api/students` - JSON API for students

## Contributing

This project is part of the Oracle Internship Program. Feel free to enhance the system with additional features such as:

- User authentication and authorization
- Advanced reporting and analytics
- Email notifications
- File upload capabilities
- Export functionality (PDF, Excel)
- REST API expansion

## License

This project is open source and available under the MIT License.

## Support

For any questions or issues with the EduFlow Student Management System, please refer to the project documentation or contact the development team.

---

**EduFlow** - Modern Student Management for Educational Excellence 🎓
