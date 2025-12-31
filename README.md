# EduFlow - Student Management System

A basic web-based Student Management System built with Python Flask and Bootstrap.

## Features

- **Dashboard**: Overview of student statistics
- **Student Management**: Add, edit, delete, and view students
- **Responsive Design**: Works on desktop and mobile devices
- **Data Persistence**: Student data stored in JSON format
- **Modern UI**: Built with Bootstrap 5 and Font Awesome icons

## Requirements

- Python 3.7 or higher
- pip package manager

## Installation

1. Navigate to the project directory:
   ```bash
   cd "EduFlow – Student Management System"
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Option 1: Direct Python (Development)
1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

### Option 2: Docker (Production)
1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Or build and run with Docker:
   ```bash
   # Build the image
   docker build -t eduflow .
   
   # Run the container
   docker run -p 5000:5000 -v $(pwd)/data:/app/data eduflow
   ```

3. Access the application at:
   ```
   http://localhost:5000
   ```

### Docker Notes:
- Data is persisted in the `./data` directory
- The application runs as a non-root user for security
- Health checks are enabled for monitoring
- The container will automatically restart unless stopped manually

## Usage

### Adding Students
1. Click "Add New Student" button
2. Fill in the required information (Name, Email, Phone, Course)
3. Click "Add Student" to save

### Managing Students
- **View**: Go to Students page to see all students
- **Edit**: Click the edit icon next to a student
- **Delete**: Click the delete icon (with confirmation)

### Dashboard
- View total students count
- See active students statistics
- Quick access to recent students

## File Structure

```
EduFlow – Student Management System/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── students.json          # Student data storage (created automatically)
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Dashboard page
│   ├── students.html     # Students list page
│   ├── add_student.html  # Add student form
│   └── edit_student.html # Edit student form
└── static/               # Static files (CSS, JS, images)
```

## Data Storage

Student data is stored in `students.json` file in the project root. The file is created automatically when you add your first student.

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Data Storage**: JSON files

## Future Enhancements

- User authentication and authorization
- Database integration (SQLite/PostgreSQL)
- Course management
- Grade tracking
- Attendance system
- Report generation
- Export functionality (PDF/Excel)

## Support

For any issues or questions, please check the console output when running the application.
