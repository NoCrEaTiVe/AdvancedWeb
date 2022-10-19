from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomUser(User):
    USER_TYPE = 'ADMIN'
    type = models.CharField(max_length=255, null=False)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.type = self.USER_TYPE
        super(CustomUser, self).save(*args, **kwargs)
