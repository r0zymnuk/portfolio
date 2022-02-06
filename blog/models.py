from django.db import models


class Posts(models.Model):
    title = models.CharField('Title', max_length=250)
    main_text = models.TextField('Post content', blank=True)
    pub_date = models.DateTimeField('Publication date', auto_now=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'posts'
