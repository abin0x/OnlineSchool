from rest_framework import serializers
from .models import Enrollment
from users.serializers import UserSerializer
from courses.serializers import CourseSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at']
