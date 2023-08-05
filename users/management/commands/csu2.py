from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@test.ru',
            first_name='Test',
            last_name='Test',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('456852')
        user.save()
