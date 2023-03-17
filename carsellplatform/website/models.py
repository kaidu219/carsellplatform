from django.db import models
import uuid


class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4, blank=False, editable=False, primary_key=True)
    first_name = models.CharField(max_length=250, null=False, verbose_name = 'Имя')
    last_name = models.CharField(max_length=250, null=False, verbose_name = 'Фамилия')
    designation = models.CharField(max_length=250, null=False, verbose_name = 'Должность')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', null=True, default="photo/withoutavatar.jpg")
    fb_link = models.URLField(max_length=200, blank=True, verbose_name = 'Ссылка на facebook')
    tw_link = models.URLField(max_length=200, blank=True, verbose_name = 'Ссылка на twitter')
    wa_link = models.URLField(max_length=200, blank=True, verbose_name = 'Ссылка на whatsapp')
    te_link = models.URLField(max_length=200, blank=True, verbose_name = 'Ссылка на telegram')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def Meta():
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
    