from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from school.models import Course, Lessons
from users.models import User
from rest_framework.test import APITestCase, APIClient


class CourseTestCase(APITestCase):
    """Тесты модели Course"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@yandex.ru',
            first_name='Test',
            last_name='Test',
            is_staff=False,
            is_superuser=False
        )

        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.url_course_create = '/course/create/'

    def test_create_course(self):
        """Тест создания модели Course"""
        data = {
            'title': 'course_test',
            'description': 'test test'
        }
        response = self.client.post(self.url_course_create, data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
