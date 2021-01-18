from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default='No bio')
    profile_pic = models.ImageField(upload_to = 'pictures/', null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()     

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    image_caption = models.CharField(max_length =30)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    




    def delete_image(self):
        self.delete()    

    def save_image(self):
        self.save()    

    def get_absolute_url(self):
        return f"/post/{self.id}"    

    class Meta:
        ordering = ['date']    

    def total_likes(self):
        return self.likes.count()    

    def __str__(self):
        return self.name    

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["-pk"]