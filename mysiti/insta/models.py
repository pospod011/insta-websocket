from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='user_profile/')
    website = models.URLField(null=True, blank=True)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_user_follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_following')
    created_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post')
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    video = models.FileField(upload_to='post_video/', null=True, blank=True)
    description = models.TextField()
    hashtag = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_comment')
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='commentlike_user')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'comment')


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='store_user')
    image = models.ImageField(upload_to='store_image/', null=True, blank=True)
    video = models.FileField(upload_to='store_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='saves')
    created_date = models.DateTimeField(auto_now_add=True)


class SaveItem(models.Model):
    cart = models.ForeignKey(Save, related_name='item', on_delete=models.CASCADE)
    post_item = models.ForeignKey(Post, related_name='post_item', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    auther = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='message_image/', null=True, blank=True)
    video = models.FileField(upload_to='message_video/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)


# .env
# filter(hashtag), search(username), order(post(created_at))
# translate(+2)
# pagination
# swagger
# permission
# jwt