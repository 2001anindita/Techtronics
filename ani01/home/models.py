from django.db import models

class Quora(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta():
        db_table="project"

class question(models.Model):
    id = models.IntegerField().primary_key
    author = models.EmailField(max_length=256)
    question = models.TextField(max_length=200)
    # description = models.CharField(max_length=100)
    # img=models.ImageField(upload_to="images", null=True, blank=True)
    def __str__(self):
        return self.question

class answer(models.Model):
    id = models.IntegerField().primary_key
    author = models.EmailField(max_length=256)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=300)
    # description = models.CharField(max_length=100)
    # img=models.ImageField(upload_to="images", null=True, blank=True)
    def __str__(self):
        return self.author

class comment(models.Model):
    id = models.IntegerField().primary_key
    author = models.TextField(max_length=256)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    def __str__(self):
        return self.author





