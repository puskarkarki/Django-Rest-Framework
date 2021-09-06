from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:

        verbose_name = 'To_do_list'
        db_table = 'todo_app'

    def __str__(self):
        return self.title
