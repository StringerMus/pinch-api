from django.db import models
from django.contrib.auth.models import User

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
        max_length=15, choices=CATEGORIES, default=null)
    #price = models.TextField(blank=True)
    #location = 
    #contact_email = 
    image = models.ImageField(
        upload_to='images/', default='../default_post_iagkbz', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'