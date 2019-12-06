from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
       
    def get_absolute_url(self):
        return "/posts/{}/".format(self.slug)

    def get_update_url(self):
        return "/posts/{}/update/".format(self.slug)

    def get_delete_url(self):
        return "/posts/{}/delete/".format(self.slug)

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    mobile_num = models.IntegerField()  # "+27"
    
    def __str__(self):
        return self.user.username

