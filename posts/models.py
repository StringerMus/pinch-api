from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator
from decimal import Decimal

CATEGORIES = (
    ('diy', 'DIY'),
    ('gardening', 'GARDENING'),
    ('gadgets', 'GADGETS'),
    ('camera', 'CAMERA'),
    ('sports', 'SPORTS'),
    ('wedding', 'WEDDING'),
    ('other', 'OTHER'),
)

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=15, choices=CATEGORIES, default='other')
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='GBP',
        default='0.00',
        validators=[MinValueValidator(Decimal('0.01'))])
    location = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length = 254)
    image = models.ImageField(
        upload_to='images/', default='../default_post_iagkbz', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.item_name}'