from django.db import models
from phone_field import PhoneField

class ContactPhone(models.Model):
    name = models.CharField(max_length=128)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
            return self.phone


