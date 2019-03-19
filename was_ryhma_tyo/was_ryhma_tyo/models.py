from django.db import models
from was_ryhma_tyo.utils.utils import generate_token

class Announcements(models.Model):
    title = models.CharField(max_length=55)
    creation_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    expiration_date = models.DateTimeField()
    custom_text = models.CharField(max_length=255)
    category = models.CharField(max_length=55, choices=[('Selling', 'Selling'),('Buying', 'Buying')], default='Selling')


    def __str__(self):
        return self.name
