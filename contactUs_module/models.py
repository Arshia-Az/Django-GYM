from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}  /  {self.email}'

    class Meta:
        verbose_name_plural = 'Contact us'
        verbose_name = 'Contact'