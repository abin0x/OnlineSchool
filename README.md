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


API Endpoints
The project has the following API endpoints:

POST /api/register/ - User registration <br>
POST /api/login/ - User login<br>
GET /api/courses/ - List all courses<br>
POST /api/courses/ - Create a new course (teachers only)<br>
GET /api/courses/{id}/ - Get details of a specific course<br>
PUT /api/courses/{id}/ - Update a specific course (teachers only)<br>
DELETE /api/courses/{id}/ - Delete a specific course (teachers only)<br>
GET /api/enrollments/ - Get enrollment history (students only)<br>






Model/Schemas
The following models are used in the project:

User
username: CharField
email: EmailField
password: CharField
Course
title: CharField
description: TextField
instructor: ForeignKey (User)
created_at: DateTimeField
Enrollment
student: ForeignKey (User)
course: ForeignKey (Course)
enrolled_at: DateTimeField
