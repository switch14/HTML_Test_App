from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100, verbose_name='名前')
    belonging = models.CharField(max_length=100, verbose_name='所属')
    hobby = models.CharField(max_length=200, verbose_name='趣味（カンマ区切りで複数入力可）')

    def __str__(self):
        return self.name