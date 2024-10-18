# Online School

👤 **Name**: Mahmudul Hasan Abin  
📚 **Project Name**: Online School  
🔗 **Live Link**: [Online School](https://lnkd.in/g9_WCKjw)

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

POST /api/register/ - User registration
POST /api/login/ - User login
GET /api/courses/ - List all courses
POST /api/courses/ - Create a new course (teachers only)
GET /api/courses/{id}/ - Get details of a specific course
PUT /api/courses/{id}/ - Update a specific course (teachers only)
DELETE /api/courses/{id}/ - Delete a specific course (teachers only)
GET /api/enrollments/ - Get enrollment history (students only)
