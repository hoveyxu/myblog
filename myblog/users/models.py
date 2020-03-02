from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # 手机号码
    mobile = models.CharField(max_length=11)

    class Meta:
        db_table = 'User'
        verbose_name="用户"