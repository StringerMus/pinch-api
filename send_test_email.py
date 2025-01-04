from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Test email functionality'

    def handle(self, *args, **kwargs):
        send_mail(
            'Test Email',
            'This is a test email from Django.',
            'mussali.one@gmail.com',  # Replace with your "from" email
            ['mussali.one@gmail.com'],  # Replace with a valid recipient email
            fail_silently=False,
        )
        self.stdout.write(self.style.SUCCESS('Test email sent successfully!'))
