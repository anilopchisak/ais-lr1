from django.db import models

class Animal(models.Model):
    pic = models.ImageField(upload_to='media', blank=True)
    fname = models.CharField('First name', max_length=255)
    sname = models.CharField('Second name', max_length=255)
    phone = models.TextField('Phone number')
    role = models.CharField('Role in the group', max_length=255)

    def __str__(self):
        return self.fname

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'