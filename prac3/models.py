from django.db import models

# Create your models here.
class Question(models.Model):
    question_str = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published Date')

    def __str__(self):
        return self.question_str.__str__()

class Choice(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_str = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_str.__str__()