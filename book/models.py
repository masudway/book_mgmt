from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100, null=True)
    published_year = models.PositiveBigIntegerField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return self.title + ' | ' + self.author + ' | ' + str(self.published_date)
