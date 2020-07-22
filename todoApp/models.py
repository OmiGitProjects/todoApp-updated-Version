from datetime import datetime
from django.db import models

class TodoDatabase(models.Model):

    todo_id = models.AutoField(primary_key=True)
    todo_task = models.TextField(max_length=500)
    slug = models.IntegerField()
    timeStamp = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return str(self.todo_id) + ' ' + str(self.timeStamp)