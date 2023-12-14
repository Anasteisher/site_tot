from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=50, blank=False)
    mail = models.CharField(max_length=40, blank=False)
    feedback = models.CharField(max_length=400, blank=False)


    def __str__(self):
        return f'{self.name} - {self.mail}'

class DogComment (models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=40, blank=False)
    feedback = models.CharField(max_length=400, blank=False)
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name} ; {self.email} ; {self.feedback} ; {self.checkbox}'