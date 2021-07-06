from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    describe = models.CharField(max_length=1000)
    body = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.comment

