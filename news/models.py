from django.db import models

class Articles(models.Model):
    title = models.CharField('Name of title', max_length=50)
    announcement = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date of publishing')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
