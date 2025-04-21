from django.db import models
from django.contrib.auth.models import User


class StoryFeedback(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    story_title = models.CharField(max_length=255)
    story_creator = models.CharField(max_length=255)  
    category = models.CharField(max_length=255)       
    
    image = models.ImageField(
        upload_to='images/', default='../default_post_rvs8fh', blank=True
    )
    your_feedback = models.TextField(blank=True)  

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.story_title}'
