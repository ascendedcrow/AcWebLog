from django.utils.timezone import now
from django.db import models
from django.conf import settings

from app.models import BaseModel

class Post(BaseModel):
    title = models.CharField('Title', max_length=255, blank=False,  null=False, unique=True)
    contents = models.TextField('Contents', max_length=255, blank=False,  null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_user', blank=False,  null=False)
    published = models.DateTimeField(blank=False, null=False, default=now)

    @property
    def future_post(self):
        return now() < self.published

    def __str__(self):
        return '{date}: {title}'.format(date=self.created.strftime("%d/%m/%Y"), title=self.title)