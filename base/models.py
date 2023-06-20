from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from base.utils import count_text




def upload_to(instance, filename):
    # Define the upload path for the audio field
    return 'posts/{}/{}'.format(instance.author.full_name, filename)



class Post(models.Model):
    audio = models.FileField(_("Audio"), upload_to=upload_to, default='posts/default.mp3')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    word_count = models.PositiveIntegerField(default=0)  # New field for word count
    objects = models.Manager()  # default manager


    class Meta:
        ordering = ('word_count',)

    def __str__(self):
        return self.author.full_name

    def save(self, *args, **kwargs):
        self.word_count = len(self.content.split())  # Calculate and update word count
        super().save(*args, **kwargs)

