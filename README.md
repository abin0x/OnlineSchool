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
1. Ensure Django is installed. If not, install it using:
   ```bash
   pip install Django


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
