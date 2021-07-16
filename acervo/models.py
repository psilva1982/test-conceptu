from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30,)
    author = models.CharField(max_length=80)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.PROTECT)
    num_pages = models.IntegerField(validators=[MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('name', 'author', 'user')