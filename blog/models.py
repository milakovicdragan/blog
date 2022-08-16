from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title
    #It says to use the URL named post_detail and pass in the pk
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk" : self.pk})
