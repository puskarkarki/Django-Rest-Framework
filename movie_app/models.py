from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Movie_Name'
        verbose_name_plural = 'Movies'
        db_table = 'movie'
    
