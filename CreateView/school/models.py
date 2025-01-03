from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=70)

    # def get_absolute_url(self):
    #     return reverse('thankyou')
    def get_absolute_url(self):
        return reverse("detailview", kwargs={"pk": self.pk})
    