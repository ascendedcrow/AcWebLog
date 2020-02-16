from app.models import BaseModel
from posts.models import Post
from django.db import models

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField('Name', max_length=255, blank=False,  null=False)
    e_mail = models.EmailField('E-Mail', max_length=255, blank=False,  null=False)
    contents = models.TextField('Contents', blank=False,  null=False)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self):
        return '{name} ({email})'.format(email=self.e_mail, name=self.contents)

    def approve_comment(self):
        self.approved = True
        self.save()
