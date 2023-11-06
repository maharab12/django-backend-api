from django.db import models

# Create your models here.


from django.db import models

class Todo(models.Model):
    title= models.CharField(max_length=50)
    des=models.CharField(max_length=200)
    isDone=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title[:20]

