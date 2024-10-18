# Online School

👤 **Name**: Mahmudul Hasan Abin  
📚 **Project Name**: Online School  
🔗 **Live Link**: [Online School](https://lnkd.in/g9_WCKjw)

<p align="center"><img src="https://i.ibb.co.com/Q6vcrjq/77912647-e7bb-46fa-ab03-3155bd34d828.png" alt="project-image"></p>

<h2>🚀 Demo</h2>

## Description
Online School is an innovative e-learning platform designed to offer a wide range of courses for learners. It provides an intuitive interface for users to sign up, log in, and enroll in courses. Students can view teacher profiles and track their course enrollments while teachers can create, edit, update, or delete courses. The platform also allows users to explore detailed course information, read blogs, and check reviews. Please note that course enrollment is restricted to logged-in users to ensure a secure learning environment.

## 🚀 Features
- Easy sign-up and login for users.
- Students can view teacher profiles and track course enrollments.
- Teachers can create, edit, update, and delete courses.
- Detailed course information accessible to all users.
- Blog reading and review-checking functionalities.
- Secure learning environment with enrollment restrictions for logged-in users.

## 💻 Technology Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django, Django REST Framework
- **Database**: SQLite3

## 🛠️ Installation Steps
<p align="center"><img src="" alt="project-image"></p>

<h2>🚀 Demo</h2>

<h2>🛠️ Installation Steps:</h2>

<p>1. Python 3.x installed.</p>

<p>2. Django installed. If not you can install it using</p>

```
pip install Django
```

<p>3. Clone the repository</p>

```
git clone https://github.com/abin0x/online-school.git
```

<p>4. Navigate to the project directory</p>

```
cd online-school
```

<p>5. Create a virtual environment</p>

```
python -m venv venv
```

<p>6. Activate the virtual environment</p>

```
venv\Scripts\activate
```

<p>7. Install the required packages</p>

```
pip install -r requirements.txt
```

<p>8. Run database migrations</p>

```
python manage.py migrate
```

<p>9. Create a superuser for accessing the admin panel</p>

```
python manage.py createsuperuser
```

<p>10. Start the Django development server</p>

```
python manage.py runserver
```

<p>11. Open your browser and go to http://127.0.0.1:8000 to access the application</p>


## API Endpoints

The project has the following API endpoints:

- **POST** `/api/register/`  
  User registration.

- **POST** `/api/login/`  
  User login.

- **GET** `/api/courses/`  
  List all courses.

- **POST** `/api/courses/`  
  Create a new course (teachers only).

- **GET** `/api/courses/{id}/`  
  Get details of a specific course.

- **PUT** `/api/courses/{id}/`  
  Update a specific course (teachers only).

- **DELETE** `/api/courses/{id}/`  
  Delete a specific course (teachers only).

- **GET** `/api/enrollments/`  
  Get enrollment history (students only).







# Project Models/Schemas

This document outlines the models used in the project, detailing the attributes of each model along with their data types.

## Models

### User
The `User` model represents the users of the application, including both students and instructors.

- **username**: `CharField`  
  A unique identifier for the user.

- **email**: `EmailField`  
  The user's email address, used for notifications and communications.

- **password**: `CharField`  
  The user's password for authentication purposes.

### Course
The `Course` model represents the educational courses available in the platform.

- **title**: `CharField`  
  The name of the course.

- **description**: `TextField`  
  A detailed description of the course content and objectives.

- **instructor**: `ForeignKey (User)`  
  A reference to the `User` model, linking the course to its instructor.

- **created_at**: `DateTimeField`  
  The timestamp indicating when the course was created.

### Enrollment
The `Enrollment` model tracks the courses that students have enrolled in.

- **student**: `ForeignKey (User)`  
  A reference to the `User` model, linking the enrollment to the student.

- **course**: `ForeignKey (Course)`  
  A reference to the `Course` model, linking the enrollment to the course.

- **enrolled_at**: `DateTimeField`  
  The timestamp indicating when the student enrolled in the course.

## Conclusion
These models provide the foundational data structure for managing users, courses, and enrollments in the project. They facilitate interactions between students and instructors while maintaining the integrity of the application's data.

