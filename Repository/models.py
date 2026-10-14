from django.db import models


# Create your models here.

class Questions(models.Model):
    title=models.CharField(max_length=200)

    Languages=(
        ("python","python"),
        ("java","java"),
        ("javascript","javascript"),
        ("c","c")
    )

    language=models.CharField(max_length=100,choices=Languages,default="python")

    Difficulty=(
        ("easy","easy"),
        ("medium","medium"),
        ("hard","hard")
    )

    difficulty=models.CharField(max_length=200,choices=Difficulty,default="easy")

    notes=models.TextField(null=True)
    topic=models.CharField(max_length=200)
    published_date=models.DateTimeField(auto_now_add=True)
    sample_input=models.TextField()
    is_active=models.BooleanField(default=True)

