from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=3000)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.question

