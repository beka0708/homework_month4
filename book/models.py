from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_data = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    def __str__(self):
        return self.title