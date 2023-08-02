from django.core.management import BaseCommand

from school.models import Course, Payment, Lessons
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.get(is_staff=False)
        user.delete()
        Course.objects.all().delete()
        Payment.objects.all().delete()

        User.objects.create(email='user@test.com', is_active=True)
        Course.objects.create(title="Django", price=5000)
        Course.objects.create(title="Основы Python", price=1000)
        User.objects.create(email='test@test.com', is_active=True)

        lessons_list = [
            {'course': Course.objects.get(title='Django'), 'title': 'Знакомство с Django',
             'description': 'Знакомство с Django'},
            {'course': Course.objects.get(title='Основы Python'), 'title': 'Циклы / часть 1',
             'description': 'часть 1'},
            {'course': Course.objects.get(title='Основы Python'), 'title': 'Циклы / часть 2',
             'description': 'часть 2'},
        ]

        payment_list = [
            {'user': User.objects.get(email='test@test.com'), 'course': Course.objects.get(title='Django'),
             'payment_method': 'наличными средствами'},
            {'user': User.objects.get(email='test@test.com'), 'course': Course.objects.get(title='Основы Python'),
             'payment_method': 'перевод на счет'},
        ]

        lessons_objects = []
        payment_objects = []

        for item in lessons_list:
            lessons_objects.append(Lessons(**item))
        Lessons.objects.bulk_create(lessons_objects)

        for item in payment_list:
            payment_objects.append(Payment(**item))
        Payment.objects.bulk_create(payment_objects)
