from django.db import models
from app.models import BaseModel

class Post(BaseModel):
    title = models.CharField('Title', max_length=255, blank=False,  null=False, unique=True)
    contents = models.TextField('Contents', max_length=255, blank=False,  null=False)

    def __str__(self):
        return '{date}: {title}'.format(date=self.created.strftime("%d/%m/%Y"), title=self.title)