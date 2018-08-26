from django.db import models

class Vote(models.Model):
    subject = models.CharField(max_length=50)
    vote_taken = models.DateTimeField(auto_now=True)
    ayes = models.PositiveIntegerField()
    nays = models.PositiveIntegerField()
