from django.core.management import BaseCommand

from school.models import Course, Payment
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        Course.objects.all().delete()
        Payment.objects.all().delete()

        Course.objects.create(title="Django", price=10)
        User.objects.create(email='test@test.com', is_active=True)

        payment_list = [
            {'course': Course.objects.get(title='Django'), 'payment_method': 'наличными средствами'},
            {'user': User.objects.get(email='test@test.com'), 'course': Course.objects.get(title='Django'),
             'payment_method': 'наличными средствами'},
        ]

        payment_objects = []

        for item in payment_list:
            payment_objects.append(Payment(**item))
        Payment.objects.bulk_create(payment_objects)
