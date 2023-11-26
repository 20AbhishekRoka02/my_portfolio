from django.db import models

# Create your models here.
class InterestUser(models.Model):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  # Adjust the max_length as needed
    email_address = models.EmailField()
    email_subject = models.CharField(max_length=255)
    message_body = models.TextField()

    def __str__(self):
        return self.fullname