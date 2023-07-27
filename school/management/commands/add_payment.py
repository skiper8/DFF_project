from django.core.management import BaseCommand

from school.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        Payment.objects.all().delete()

        payment_list = [
            {'course': 'Django', 'payment_method': 'наличными средствами'},
            {'user': 3, 'course': 11, 'payment_method': 'наличными средствами'},
        ]

        payment_objects = []

        for item in payment_list:
            payment_objects.append(Payment(**item))
        Payment.objects.bulk_create(payment_objects)
