from django.db import models



class Contact(models.Model):
    ur_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
