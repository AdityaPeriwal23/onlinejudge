from django.db import models

class User(models.Model):
    username = models.TextField("kjxnwek")
    password = models.TextField("buhw")

class Problem(models.Model):
    y=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    statement = models.TextField()
    difficulty = models.IntegerField(default=0)
    solved_status = models.BooleanField()
    
class TestCases(models.Model):
    question = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_text = models.TextField()
    output_text = models.TextField()

class Submissions(models.Model):
    qwerty=models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Problem, on_delete=models.CASCADE)
    coder = models.TextField("C++")
    useroutput=models.TextField("xyz")
    sub_date = models.DateTimeField('Submitted at')
    verdict = models.BooleanField()